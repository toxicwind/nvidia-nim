#!/usr/bin/env python3
"""probe.py — fail-fast per-model diagnostic ladder for NVIDIA NIM.

Treats the API as an unreliable narrator: /v1/models lists 82 models, but
listing != usable. For each model, run a diagnostic ladder that
distinguishes DEAD (404/410) from SLOW (cold-start latency) from
STREAMING-BROKEN, instead of one mushy pass/fail:

  Phase A (fail fast): tiny non-streaming completion, max_tokens=3,
      timeout 12s. 200=alive, 404=gated, 410=eol, 429=rate-limited,
      timeout=ambiguous -> Phase C.
  Phase B (streaming): stream max_tokens=10, close after first content
      chunk. Records TTFT; timeout 25s. Catches streaming stalls on
      models whose non-streaming path works.
  Phase C (slow retry): only if Phase A timed out. One retry, timeout 60s.
      ok = alive but cold-start slow (latency issue, not dead).

Verdicts: alive-fast, alive, alive-slow-coldstart, streaming-stall,
           dead-404-gated, dead-410-eol, rate-limited-429, flaky-timeout,
           error-other.

Usage:
  probe.py [--all] [--timeout-a 12] [--timeout-c 60] [--out results.json]
  --all probes every id in the live /v1/models catalog (82); default
  probes the 18 models in the ranking skill table.

Every run appends one JSON line per model to probe_audit.jsonl
(first-class audit with timings).
"""
from __future__ import annotations

import argparse
import datetime as dt
import importlib.util
import json
import re
import sys
import time
import urllib.request

sys.path.insert(0, "/opt/hatch/skills/skill-creator/bin")
from dynamic_credentials import add_surrogate_to_request

BASE = "https://integrate.api.nvidia.com/v1"
CRED = "custom.nvidia"
HOSTS = ["integrate.api.nvidia.com"]
AUDIT = "/home/hatch/workspace/skills/nvidia-nim-loader/probe_audit.jsonl"
RANK_PY = "/home/hatch/workspace/skills/model-ranking/bin/rank.py"


INTERESTING_HEADERS = ("deprecation", "nvcf-status", "nvcf-reqid")


def pick_headers(hdrs):
    try:
        return {k.lower(): v for k, v in hdrs.items()
                if k.lower() in INTERESTING_HEADERS}
    except Exception:
        return {}


def tiny_completion(model, timeout, max_tokens=3, stream=False):
    """Maximal-debug completion probe. Returns a dict: ok, status, lat_ms,
    ttfb_ms (None when headers never arrived — distinguishes connect/header
    stalls from body stalls), ttft_ms, detail, headers (deprecation /
    nvcf-status / nvcf-reqid), sched (live NVCF scheduler snapshot),
    eol_date (parsed from 410 bodies)."""
    payload = {"model": model,
               "messages": [{"role": "user", "content": "Reply with the single word OK"}],
               "max_tokens": max_tokens, "temperature": 0}
    if stream:
        payload["stream"] = True
    req = urllib.request.Request(
        f"{BASE}/chat/completions", data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"}, method="POST")
    add_surrogate_to_request(req, CRED, allowed_hosts=HOSTS)
    t0 = time.monotonic()
    ttft = None
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            ttfb_ms = round((time.monotonic() - t0) * 1000, 1)
            hdrs = pick_headers(resp.headers)
            if not stream:
                body = resp.read().decode()
                d = json.loads(body)
                content = d["choices"][0]["message"].get("content")
                sched = ((d.get("nvext") or {}).get("scheduler_snapshot")) or {}
                return {"ok": True, "status": resp.status,
                        "lat_ms": round((time.monotonic() - t0) * 1000, 1),
                        "ttfb_ms": ttfb_ms, "ttft_ms": None,
                        "detail": (content or "")[:60], "headers": hdrs,
                        "sched": sched}
            # streaming: read until first content delta, then bail
            for raw in resp:
                line = raw.decode("utf-8", errors="replace").strip()
                if not line.startswith("data:"):
                    continue
                data = line[5:].strip()
                if data == "[DONE]":
                    break
                if ttft is None:
                    ttft = (time.monotonic() - t0) * 1000
                try:
                    chunk = json.loads(data)
                except json.JSONDecodeError:
                    continue
                for ch in chunk.get("choices", []):
                    delta = ch.get("delta", {}) or {}
                    if delta.get("content") or delta.get("tool_calls"):
                        return {"ok": True, "status": resp.status,
                                "lat_ms": round((time.monotonic() - t0) * 1000, 1),
                                "ttfb_ms": ttfb_ms, "ttft_ms": round(ttft, 1),
                                "detail": "stream-chunk-ok", "headers": hdrs,
                                "sched": {}}
            return {"ok": True, "status": resp.status,
                    "lat_ms": round((time.monotonic() - t0) * 1000, 1),
                    "ttfb_ms": ttfb_ms,
                    "ttft_ms": round(ttft, 1) if ttft else None,
                    "detail": "stream-empty", "headers": hdrs, "sched": {}}
    except urllib.error.HTTPError as e:
        lat_ms = round((time.monotonic() - t0) * 1000, 1)
        try:
            detail = e.read().decode()[:400]
            hdrs = pick_headers(e.headers)
        except Exception:
            detail, hdrs = "", {}
        r = {"ok": False, "status": e.code, "lat_ms": lat_ms,
             "ttfb_ms": lat_ms, "ttft_ms": None, "detail": detail,
             "headers": hdrs, "sched": {}}
        m = re.search(r"end of life on (\S+)", detail)
        if m:
            r["eol_date"] = m.group(1)
        return r
    except Exception as e:
        return {"ok": False, "status": type(e).__name__,
                "lat_ms": round((time.monotonic() - t0) * 1000, 1),
                "ttfb_ms": None, "ttft_ms": None,
                "detail": str(e)[:160], "headers": {}, "sched": {}}


def diagnose(model, t_a=12, t_c=60, slow=True):
    """Run the ladder. Returns a dict with verdict + evidence."""
    rec = {"model": model, "ts": dt.datetime.now(dt.timezone.utc).isoformat()}
    a = tiny_completion(model, t_a)
    rec["phase_a"] = {"ok": a["ok"], "status": a["status"],
                      "lat_ms": a["lat_ms"], "ttfb_ms": a["ttfb_ms"],
                      "detail": a["detail"][:120], "headers": a["headers"]}
    if a.get("sched"):
        rec["phase_a"]["sched"] = a["sched"]
    if a.get("eol_date"):
        rec["eol_date"] = a["eol_date"]
    if a["ok"]:
        verdict = "alive-fast" if a["lat_ms"] < 5000 else "alive"
        # Phase B: streaming check
        b = tiny_completion(model, 25, 10, stream=True)
        rec["phase_b"] = {"ok": b["ok"], "status": b["status"],
                          "lat_ms": b["lat_ms"], "ttfb_ms": b["ttfb_ms"],
                          "ttft_ms": b["ttft_ms"],
                          "detail": str(b["detail"])[:80],
                          "headers": b["headers"]}
        if not b["ok"] and b["status"] in ("timeout", "TimeoutError"):
            verdict = ("streaming-stall" if b["ttfb_ms"] is not None
                       else "streaming-noheaders")
        elif not b["ok"]:
            verdict = "alive-nostream-err"
        rec["verdict"] = verdict
    elif a["status"] == 404:
        rec["verdict"] = "dead-404-gated"
    elif a["status"] == 410:
        rec["verdict"] = "dead-410-eol"
    elif a["status"] == 429:
        rec["verdict"] = "rate-limited-429"
    elif a["status"] == 503:
        rec["verdict"] = "unavailable-503"
    elif a["status"] in ("timeout", "TimeoutError", "socket.timeout", "URLError"):
        if not slow:
            # super fail-fast: no slow retry, timeout is the verdict
            rec["verdict"] = "timeout-fast"
        else:
            # Phase C: ambiguous timeout -> one slow retry to separate
            # cold-start latency from actually-dead
            c = tiny_completion(model, t_c)
            rec["phase_c"] = {"ok": c["ok"], "status": c["status"],
                              "lat_ms": c["lat_ms"], "ttfb_ms": c["ttfb_ms"],
                              "detail": str(c["detail"])[:120],
                              "headers": c["headers"]}
            rec["verdict"] = ("alive-slow-coldstart" if c["ok"]
                              else "flaky-timeout")
    else:
        rec["verdict"] = "error-other"
    return rec


def load_ranked_models():
    spec = importlib.util.spec_from_file_location("rankmod", RANK_PY)
    rankmod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(rankmod)
    return [m["id"] for m in rankmod.MODELS]


def load_catalog_models():
    req = urllib.request.Request(f"{BASE}/models", method="GET")
    add_surrogate_to_request(req, CRED, allowed_hosts=HOSTS)
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.load(resp)
    return [m["id"] for m in data.get("data", [])]


def main():
    ap = argparse.ArgumentParser(description="fail-fast NIM per-model diagnostic ladder")
    ap.add_argument("--all", action="store_true",
                    help="probe every id in the live /v1/models catalog")
    ap.add_argument("--timeout-a", type=float, default=12)
    ap.add_argument("--timeout-c", type=float, default=60)
    ap.add_argument("--sleep", type=float, default=1.0)
    ap.add_argument("--workers", type=int, default=1,
                    help="parallel diagnose workers (default 1 = sequential)")
    ap.add_argument("--no-slow", action="store_true",
                    help="super fail-fast: skip Phase C slow retry; "
                         "timeouts get verdict timeout-fast")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    models = load_catalog_models() if args.all else load_ranked_models()
    print(f"probing {len(models)} models (fail-fast ladder, "
          f"workers={args.workers})\n", flush=True)
    results = (run_parallel(models, args) if args.workers > 1
               else run_sequential(models, args))
    print_summary(results, args)
    return 0


def run_sequential(models, args):
    results = []
    with open(AUDIT, "a") as audit:
        for i, m in enumerate(models):
            rec = diagnose(m, args.timeout_a, args.timeout_c,
                           slow=not args.no_slow)
            results.append(rec)
            audit.write(json.dumps(rec) + "\n")
            audit.flush()
            v = rec["verdict"]
            a = rec["phase_a"]
            extra = ""
            if "phase_b" in rec and rec["phase_b"].get("ttft_ms"):
                extra = f" ttft={rec['phase_b']['ttft_ms']}ms"
            print(f"[{i+1}/{len(models)}] {m}\n"
                  f"    {v} | A:{a['status']} {a['lat_ms']}ms{extra}", flush=True)
            if v == "rate-limited-429":
                print("    429 hit — backing off 60s", flush=True)
                time.sleep(60)
            elif i < len(models) - 1:
                time.sleep(args.sleep)
    return results


def run_parallel(models, args):
    """Bounded-concurrency diagnose: global 429 backoff + min 1s between
    model starts, audit writes and progress prints serialized."""
    import threading
    from concurrent.futures import ThreadPoolExecutor, as_completed
    lock = threading.Lock()
    backoff = {"until": 0.0, "last_start": 0.0}
    results = [None] * len(models)
    audit = open(AUDIT, "a")

    def gated_diagnose(i, m):
        while True:  # global 429 backoff + start pacing
            with lock:
                now = time.monotonic()
                wait = max(backoff["until"] - now,
                           1.0 - (now - backoff["last_start"]), 0)
                if wait <= 0:
                    backoff["last_start"] = time.monotonic()
                    break
            time.sleep(min(wait, 2))
        rec = diagnose(m, args.timeout_a, args.timeout_c,
                       slow=not args.no_slow)
        a = rec["phase_a"]
        extra = ""
        if "phase_b" in rec and rec["phase_b"].get("ttft_ms"):
            extra = f" ttft={rec['phase_b']['ttft_ms']}ms"
        with lock:
            if rec["verdict"] == "rate-limited-429":
                backoff["until"] = time.monotonic() + 60
                print("    429 hit — global backoff 60s", flush=True)
            audit.write(json.dumps(rec) + "\n")
            audit.flush()
            print(f"[{i+1}/{len(models)}] {m}\n"
                  f"    {rec['verdict']} | A:{a['status']} {a['lat_ms']}ms{extra}",
                  flush=True)
        return i, rec

    try:
        with ThreadPoolExecutor(max_workers=args.workers) as ex:
            futs = [ex.submit(gated_diagnose, i, m)
                    for i, m in enumerate(models)]
            for f in as_completed(futs):
                i, rec = f.result()
                results[i] = rec
    finally:
        audit.close()
    return results


def print_summary(results, args):
    print("\n== verdict summary ==")
    from collections import Counter
    for v, c in Counter(r["verdict"] for r in results).most_common():
        print(f"  {v}: {c}")
    print("\n== usable now (alive-*) ==")
    for r in results:
        if r["verdict"].startswith("alive"):
            b = r.get("phase_b", {})
            print(f"  {r['model']}: {r['verdict']} "
                  f"A={r['phase_a']['lat_ms']}ms ttft={b.get('ttft_ms')}ms")
    print("\n== deprecation warnings (from response headers) ==")
    seen = set()
    for r in results:
        for ph in ("phase_a", "phase_b"):
            dep = (r.get(ph) or {}).get("headers", {}).get("deprecation")
            if dep and r["model"] not in seen:
                seen.add(r["model"])
                print(f"  {r['model']}: deprecated {dep}")
    if not seen:
        print("  none")
    if args.out:
        json.dump(results, open(args.out, "w"), indent=2)
        print(f"\nwrote {args.out}")
    print(f"audit appended to {AUDIT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
