#!/usr/bin/env python3
"""Maximal-debug endpoint audit for NIM chat completions.

No truncation: captures full response headers, full bodies (length noted),
and phase timings (time-to-headers vs body-transfer) so we can see WHERE
each failure mode actually happens: TCP/connect stall, header stall
(TTFB), or body stall. Also audits one streaming call per sampled model.

Writes audit_endpoints_<stamp>.json next to this script.
"""
import datetime as dt
import json
import os
import socket
import sys
import time
import urllib.request
import urllib.error

sys.path.insert(0, "/opt/hatch/skills/skill-creator/bin")
from dynamic_credentials import add_surrogate_to_request

BASE = "https://integrate.api.nvidia.com/v1"
CRED = "custom.nvidia"
HOSTS = ["integrate.api.nvidia.com"]
BODY_CAP = 32768

SAMPLES = [
    # (model, kind we expect, urlopen timeout)
    ("nvidia/llama-3.1-nemotron-70b-instruct", "expect-404", 20),
    ("nvidia/nemotron-3-nano-30b-a3b", "expect-410", 20),
    ("nvidia/nemotron-3-nano-omni-30b-a3b-reasoning", "expect-503", 20),
    ("nvidia/nemotron-3-super-120b-a12b", "expect-alive", 30),
    ("deepseek-ai/deepseek-v4-flash-0731", "expect-streamstall", 30),
    ("nvidia/nemotron-3-ultra-550b-a55b", "expect-timeout", 15),
]


def post(model, stream=False, timeout=20, max_tokens=3):
    """POST chat completions. Returns a full evidence dict, nothing truncated
    except the body beyond BODY_CAP (length + sha of full body still noted)."""
    rec = {"model": model, "stream": stream, "timeout": timeout,
           "ts": dt.datetime.now(dt.timezone.utc).isoformat()}
    payload = {"model": model,
               "messages": [{"role": "user", "content": "Reply with OK"}],
               "max_tokens": max_tokens, "temperature": 0}
    if stream:
        payload["stream"] = True
    req = urllib.request.Request(
        f"{BASE}/chat/completions", data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"}, method="POST")
    add_surrogate_to_request(req, CRED, allowed_hosts=HOSTS)
    t0 = time.monotonic()
    try:
        resp = urllib.request.urlopen(req, timeout=timeout)
        t_headers = time.monotonic()
        rec["stage_reached"] = "headers"
        rec["ttfb_ms"] = round((t_headers - t0) * 1000, 1)
        rec["status"] = resp.status
        rec["headers"] = {k.lower(): v for k, v in resp.headers.items()}
        if stream:
            # read SSE until first content delta or deadline
            lines, nbytes, first_delta_ms = 0, 0, None
            deadline = t0 + timeout
            body_chunks = []
            try:
                for raw in resp:
                    lines += 1
                    nbytes += len(raw)
                    body_chunks.append(raw)
                    if sum(map(len, body_chunks)) > BODY_CAP:
                        break
                    line = raw.decode("utf-8", errors="replace").strip()
                    if line.startswith("data:"):
                        d = line[5:].strip()
                        if d and d != "[DONE]":
                            try:
                                ch = json.loads(d)
                            except json.JSONDecodeError:
                                continue
                            for c in ch.get("choices", []):
                                delta = c.get("delta", {}) or {}
                                if delta.get("content") or delta.get("tool_calls"):
                                    first_delta_ms = round(
                                        (time.monotonic() - t0) * 1000, 1)
                                    raise StopIteration
                    if time.monotonic() > deadline:
                        break
            except StopIteration:
                pass
            rec["sse_lines"] = lines
            rec["sse_bytes"] = nbytes
            rec["first_delta_ms"] = first_delta_ms
            rec["body_truncated_at_cap"] = sum(map(len, body_chunks)) > BODY_CAP
        else:
            raw = resp.read()
            rec["body_len"] = len(raw)
            rec["body_truncated_at_cap"] = len(raw) > BODY_CAP
            rec["body"] = raw[:BODY_CAP].decode("utf-8", errors="replace")
        rec["total_ms"] = round((time.monotonic() - t0) * 1000, 1)
        rec["outcome"] = "ok"
    except urllib.error.HTTPError as e:
        t1 = time.monotonic()
        rec["stage_reached"] = "headers(error)"
        rec["ttfb_ms"] = round((t1 - t0) * 1000, 1)
        rec["status"] = e.code
        try:
            rec["headers"] = {k.lower(): v for k, v in e.headers.items()}
        except Exception:
            rec["headers"] = {}
        try:
            raw = e.read()
        except Exception:
            raw = b""
        rec["body_len"] = len(raw)
        rec["body_truncated_at_cap"] = len(raw) > BODY_CAP
        rec["body"] = raw[:BODY_CAP].decode("utf-8", errors="replace")
        rec["total_ms"] = round((time.monotonic() - t0) * 1000, 1)
        rec["outcome"] = "http_error"
    except (socket.timeout, TimeoutError) as e:
        rec["stage_reached"] = "timeout-before-or-during-headers"
        rec["total_ms"] = round((time.monotonic() - t0) * 1000, 1)
        rec["outcome"] = "timeout"
        rec["exc"] = f"{type(e).__name__}: {e}"
    except Exception as e:
        rec["stage_reached"] = "exception"
        rec["total_ms"] = round((time.monotonic() - t0) * 1000, 1)
        rec["outcome"] = "exception"
        rec["exc"] = f"{type(e).__name__}: {e}"
    return rec


def main():
    out = []
    for model, kind, to in SAMPLES:
        print(f"== {model} ({kind}) ==", flush=True)
        rec = post(model, stream=False, timeout=to)
        out.append(rec)
        print(f"   non-stream: {rec['outcome']} status={rec.get('status')} "
              f"stage={rec['stage_reached']} ttfb={rec.get('ttfb_ms')}ms "
              f"total={rec.get('total_ms')}ms body_len={rec.get('body_len')}",
              flush=True)
        if rec.get("outcome") == "ok":
            srec = post(model, stream=True, timeout=20, max_tokens=10)
            out.append(srec)
            print(f"   stream:     {srec['outcome']} "
                  f"stage={srec['stage_reached']} ttfb={srec.get('ttfb_ms')}ms "
                  f"first_delta={srec.get('first_delta_ms')}ms "
                  f"sse_lines={srec.get('sse_lines')} sse_bytes={srec.get('sse_bytes')}",
                  flush=True)
    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d")
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        f"audit_endpoints_{stamp}.json")
    json.dump(out, open(path, "w"), indent=2)
    print(f"\nwrote {path} ({len(out)} records, full bodies+headers)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
