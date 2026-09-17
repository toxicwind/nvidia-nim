#!/usr/bin/env python3
"""bench.py - live tool-use benchmark with streaming across NIM models.

Candidate pool comes from the model-ranking skill. Each model runs the SAME
complex multi-hop tool-use task over a streaming connection; models are then
ranked on observed data: task success, tool-call validity, turns used,
time-to-first-token, tokens/sec.

The task: three papers named by arXiv ID. The model must
  1. call get_paper_details for each (3 calls),
  2. call calculator to compute cites/year = citations / (2026 - year + 1),
  3. output the final ranking as JSON, highest cites/year first.

Expected: 1706.03762 (12000/yr) > 1810.04805 (10000/yr) > 2302.01318 (310/yr).

Some NIM models emit textual pseudo tool calls
(<tool_call><function=name>...) instead of native tool_calls; the harness
parses those as a fallback and counts them separately.

Usage:
  bench.py [--models id,id,...] [--n 5] [--max-turns 8] [--timeout 150]
           [--sleep 5] [--out results.json]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.request

import os
from auth import add_surrogate_to_request

BASE = "https://integrate.api.nvidia.com/v1"
CRED = "custom.nvidia"
HOSTS = ["integrate.api.nvidia.com"]

PAPERS_DB = {
    "2302.01318": {"title": "Accelerating Large Language Model Decoding with Speculative Sampling",
                   "year": 2023, "citations": 1240},
    "1706.03762": {"title": "Attention Is All You Need",
                   "year": 2017, "citations": 120000},
    "1810.04805": {"title": "BERT: Pre-training of Deep Bidirectional Transformers",
                   "year": 2018, "citations": 90000},
}
EXPECTED_ORDER = ["1706.03762", "1810.04805", "2302.01318"]
CURRENT_YEAR = 2026

TITLE_KEYS = {
    "1706.03762": ["attention is all you need"],
    "1810.04805": ["bert"],
    "2302.01318": ["speculative sampling"],
}

TOOLS = [
    {"type": "function", "function": {
        "name": "get_paper_details",
        "description": "Look up a paper's title, publication year and citation count by arXiv ID.",
        "parameters": {"type": "object",
                       "properties": {"arxiv_id": {"type": "string",
                                                  "description": "arXiv ID like 2302.01318"}},
                       "required": ["arxiv_id"]}}},
    {"type": "function", "function": {
        "name": "calculator",
        "description": "Evaluate an arithmetic expression and return the number.",
        "parameters": {"type": "object",
                       "properties": {"expression": {"type": "string",
                                                     "description": "e.g. '120000 / 10'"}},
                       "required": ["expression"]}}},
]

SYSTEM = (
    "You are a research assistant with tools. Think step by step, call tools "
    "as needed, then give the final answer as a single JSON object on its own "
    "line: {\"ranking\": [\"<arxiv_id>\", ...]} ordered by cites/year "
    "descending. No prose after the JSON."
)
USER_TASK = (
    "Rank these three papers by citations per year (citations / (2026 - year + 1)): "
    "2302.01318, 1706.03762, 1810.04805. "
    "Use get_paper_details for each paper, then calculator for each cites/year "
    "score, then output the final JSON ranking."
)


def tool_exec(name, args):
    if name == "get_paper_details":
        pid = str(args.get("arxiv_id", "")).strip()
        d = PAPERS_DB.get(pid)
        return json.dumps(d or {"error": "unknown paper " + pid})
    if name == "calculator":
        expr = str(args.get("expression", ""))
        if not re.fullmatch(r"[\d\s\.\+\-\*\/\(\)]+", expr):
            return json.dumps({"error": "invalid expression"})
        try:
            return json.dumps({"result": eval(expr, {"__builtins__": {}}, {})})
        except Exception as exc:
            return json.dumps({"error": str(exc)[:100]})
    return json.dumps({"error": "unknown tool " + name})


def stream_chat(model, messages, timeout):
    """One streaming chat call.

    Returns (text, tool_calls, ttft_s, total_s, out_tokens, error).
    tool_calls = [{"name":..., "args":...}] accumulated across SSE chunks.
    """
    payload = {"model": model, "messages": messages, "tools": TOOLS,
               "tool_choice": "auto", "temperature": 0.2, "max_tokens": 1024,
               "stream": True, "stream_options": {"include_usage": True}}
    req = urllib.request.Request(
        f"{BASE}/chat/completions",
        data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"}, method="POST")
    add_surrogate_to_request(req, CRED, allowed_hosts=HOSTS)
    t0 = time.monotonic()
    ttft, text_parts, tcalls, out_tokens = None, [], {}, None
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            for raw in resp:
                line = raw.decode("utf-8", errors="replace").strip()
                if not line.startswith("data:"):
                    continue
                data = line[5:].strip()
                if data == "[DONE]":
                    break
                try:
                    chunk = json.loads(data)
                except json.JSONDecodeError:
                    continue
                if ttft is None:
                    ttft = time.monotonic() - t0
                if "usage" in chunk and chunk["usage"]:
                    out_tokens = chunk["usage"].get("completion_tokens")
                for ch in chunk.get("choices", []):
                    delta = ch.get("delta", {}) or {}
                    c = delta.get("content") or delta.get("reasoning_content")
                    if c:
                        text_parts.append(c)
                    for tc in delta.get("tool_calls") or []:
                        i = tc.get("index", 0)
                        e = tcalls.setdefault(i, {"id": "", "name": "", "args": ""})
                        e["id"] += tc.get("id", "") or ""
                        fn = tc.get("function", {}) or {}
                        e["name"] += fn.get("name", "") or ""
                        e["args"] += fn.get("arguments", "") or ""
    except Exception as exc:
        return None, [], None, time.monotonic() - t0, None, str(exc)[:200]
    total = time.monotonic() - t0
    calls = []
    for e in tcalls.values():
        try:
            args = json.loads(e["args"]) if e["args"] else {}
        except json.JSONDecodeError:
            args = {"_parse_error": e["args"][:100]}
        calls.append({"name": e["name"], "args": args})
    return "".join(text_parts), calls, ttft, total, out_tokens, None


def parse_pseudo_calls(text):
    """Parse textual pseudo tool calls: <function=name> blocks containing
    <parameter=k>value pairs. Returns list of {"name","args"} dicts."""
    calls = []
    fm = re.compile(r"<function=([A-Za-z_]\w*)>")
    pm = re.compile(r"<parameter=([A-Za-z_]\w*)>([^<]*)")
    for m in fm.finditer(text or ""):
        seg = text[m.end():]
        cut = seg.find("</function>")
        seg = seg[:cut] if cut != -1 else seg[:2000]
        args = {}
        for a, b in pm.findall(seg):
            args[a] = b.strip()
        if m.group(1) in ("get_paper_details", "calculator") and args:
            calls.append({"name": m.group(1), "args": args, "pseudo": True})
    return calls


def grade(final_text):
    """Grade on the model's LAST "ranking": [...] JSON array.

    The reasoning text mentions IDs in arbitrary order, so first-appearance
    order is meaningless; the final emitted ranking is what counts.
    Falls back to title-keyword order if no ranking array is found.
    """
    t = final_text or ""
    best = None
    for m in re.finditer(r'"ranking"\s*:\s*\[(.*?)\]', t, re.S):
        ids = [i for i in re.findall(r"\d{4}\.\d{4,5}", m.group(1))
               if i in EXPECTED_ORDER]
        if ids:
            best = ids
    if best is not None:
        seen = set()
        ordered = []
        for i in best:
            if i not in seen:
                seen.add(i)
                ordered.append(i)
        return ordered == EXPECTED_ORDER, ordered
    low = t.lower()
    pos = {}
    for pid, keys in TITLE_KEYS.items():
        hits = [low.find(k) for k in keys if k in low]
        if hits:
            pos[pid] = min(hits)
    if len(pos) == 3:
        by_title = sorted(pos, key=pos.get)
        return by_title == EXPECTED_ORDER, by_title
    return False, []


def run_model(model, max_turns, timeout):
    messages = [{"role": "system", "content": SYSTEM},
                {"role": "user", "content": USER_TASK}]
    turns = 0
    made = 0
    valid = 0
    pseudo = 0
    ttfts = []
    total_s = 0.0
    out_tokens = 0
    final_text = ""
    error = None
    for _ in range(max_turns):
        turns += 1
        text, calls, ttft, tsec, otok, err = stream_chat(model, messages, timeout)
        if err:
            error = err
            break
        total_s += tsec
        if ttft is not None:
            ttfts.append(ttft)
        if otok:
            out_tokens += otok
        if not calls:
            pcalls = parse_pseudo_calls(text)
            if pcalls:
                calls = pcalls
                pseudo += len(pcalls)
        if calls:
            tcs = []
            for i, c in enumerate(calls):
                tcs.append({"id": c.get("id") or ("call_%d_%d" % (turns, i)),
                            "type": "function",
                            "function": {"name": c["name"],
                                         "arguments": json.dumps(c["args"])}})
            messages.append({"role": "assistant", "content": text or None,
                             "tool_calls": tcs})
            for i, c in enumerate(calls):
                made += 1
                name_ok = c["name"] in ("get_paper_details", "calculator")
                args_ok = isinstance(c["args"], dict) and "_parse_error" not in c["args"]
                if name_ok and args_ok:
                    valid += 1
                    result = tool_exec(c["name"], c["args"])
                else:
                    result = json.dumps({"error": "invalid tool call"})
                messages.append({"role": "tool", "tool_call_id": tcs[i]["id"],
                                 "content": result})
        else:
            final_text = text or ""
            break
    success, ordered = grade(final_text)
    tps = (out_tokens / total_s) if out_tokens and total_s else None
    return {
        "model": model,
        "success": success,
        "final_ids": ordered,
        "turns": turns,
        "tool_calls": made,
        "pseudo_tool_calls": pseudo,
        "tool_call_valid_rate": round(valid / max(made, 1), 2),
        "ttft_s": round(min(ttfts), 2) if ttfts else None,
        "total_s": round(total_s, 1),
        "out_tokens": out_tokens,
        "tok_per_s": round(tps, 1) if tps else None,
        "error": error,
    }


def pick_candidates(n):
    """Top-n models from the ranking skill, filtered to verified/listed."""
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "rankmod", os.path.join(os.path.dirname(os.path.abspath(__file__)), "rank.py"))
    rankmod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(rankmod)
    scored = sorted(
        (m for m in rankmod.MODELS if m.get("avail") in ("verified", "listed")),
        key=lambda m: rankmod.score(m, "agent"), reverse=True)
    return [m["id"] for m in scored[:n]]


def main():
    ap = argparse.ArgumentParser(description="live streaming tool-use benchmark")
    ap.add_argument("--models", default=None,
                    help="comma-separated model ids (default: top picks from ranking skill)")
    ap.add_argument("--n", type=int, default=5)
    ap.add_argument("--max-turns", type=int, default=8)
    ap.add_argument("--timeout", type=float, default=150)
    ap.add_argument("--sleep", type=float, default=5)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    models = args.models.split(",") if args.models else pick_candidates(args.n)
    print("live benchmark: %d models, streaming, tool-use task" % len(models), flush=True)
    results = []
    for i, m in enumerate(models):
        m = m.strip()
        print("[%d/%d] %s ..." % (i + 1, len(models), m), flush=True)
        r = run_model(m, args.max_turns, args.timeout)
        results.append(r)
        st = "PASS" if r["success"] else ("ERROR " + str(r["error"])[:60] if r["error"] else "FAIL")
        print("    -> %s turns=%d valid=%.2f pseudo=%d ttft=%ss total=%ss tok/s=%s" % (
            st, r["turns"], r["tool_call_valid_rate"], r["pseudo_tool_calls"],
            r["ttft_s"], r["total_s"], r["tok_per_s"]), flush=True)
        if i < len(models) - 1:
            time.sleep(args.sleep)

    ranked = sorted(results, key=lambda r: (
        not r["success"],
        -(r["tool_call_valid_rate"] or 0),
        r["turns"],
        r["total_s"] if r["total_s"] else 1e9,
    ))
    for i, r in enumerate(ranked, 1):
        r["live_rank"] = i
    print("")
    print("== live ranking (tool-use task, streaming) ==")
    for r in ranked:
        mark = "PASS" if r["success"] else "FAIL"
        print("%d. %s" % (r["live_rank"], r["model"]))
        print("   %s | valid %.2f (pseudo %d) | turns %d | ttft %ss | total %ss | tok/s %s | final %s" % (
            mark, r["tool_call_valid_rate"], r["pseudo_tool_calls"], r["turns"],
            r["ttft_s"], r["total_s"], r["tok_per_s"], r["final_ids"] or "-"))
    if args.out:
        json.dump(ranked, open(args.out, "w"), indent=2)
        print("")
        print("wrote %s" % args.out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
