#!/usr/bin/env python3
"""Fuzz the maximal NIM API surface: every endpoint/shape we can think of,
full headers + full bodies + timings. Goal: find hidden behavior —
per-model entitlement endpoints, EOL/deprecation signals, undocumented
routes, and how error shapes differ across layers.
"""
import datetime as dt
import json
import os
import sys
import time
import urllib.request
import urllib.error

sys.path.insert(0, "/opt/hatch/skills/skill-creator/bin")
from dynamic_credentials import add_surrogate_to_request

BASE = "https://integrate.api.nvidia.com/v1"
CRED = "custom.nvidia"
HOSTS = ["integrate.api.nvidia.com"]
BODY_CAP = 8192
TO = 12

CHAT_BODY = {"model": "nvidia/nemotron-3-super-120b-a12b",
             "messages": [{"role": "user", "content": "Reply with OK"}],
             "max_tokens": 3, "temperature": 0}

# (name, method, path, body_dict_or_None)
TARGETS = [
    ("models-list", "GET", "/models", None),
    ("model-get-alive", "GET", "/models/nvidia/nemotron-3-super-120b-a12b", None),
    ("model-get-gated", "GET", "/models/nvidia/llama-3.1-nemotron-70b-instruct", None),
    ("model-get-bogus", "GET", "/models/nope/not-a-model", None),
    ("model-get-eol", "GET", "/models/nvidia/nemotron-3-nano-30b-a3b", None),
    ("legacy-completions", "POST", "/completions",
     {"model": "nvidia/nemotron-3-super-120b-a12b", "prompt": "hi", "max_tokens": 3}),
    ("embeddings", "POST", "/embeddings",
     {"model": "nvidia/nv-embed-v1", "input": "hello world"}),
    ("embeddings-chat-model", "POST", "/embeddings",
     {"model": "nvidia/nemotron-3-super-120b-a12b", "input": "hello world"}),
    ("images", "POST", "/images/generations",
     {"model": "nvidia/nemotron-3-super-120b-a12b", "prompt": "a cat"}),
    ("audio-speech", "POST", "/audio/speech",
     {"model": "nvidia/nemotron-3-super-120b-a12b", "input": "hi", "voice": "alloy"}),
    ("moderations", "POST", "/moderations", {"input": "hello"}),
    ("chat-stream-options", "POST", "/chat/completions",
     {**CHAT_BODY, "stream": True, "stream_options": {"include_usage": True}}),
    ("chat-response-format", "POST", "/chat/completions",
     {**CHAT_BODY, "response_format": {"type": "json_object"}}),
    ("chat-tools-param", "POST", "/chat/completions",
     {**CHAT_BODY, "tools": [{"type": "function",
        "function": {"name": "ping", "parameters": {"type": "object", "properties": {}}}}],
       "tool_choice": "auto"}),
    ("chat-n2", "POST", "/chat/completions", {**CHAT_BODY, "n": 2}),
    ("chat-logprobs", "POST", "/chat/completions", {**CHAT_BODY, "logprobs": True}),
    ("chat-empty-model", "POST", "/chat/completions",
     {"model": "", "messages": [{"role": "user", "content": "hi"}]}),
    ("chat-no-body", "POST", "/chat/completions", {}),
    ("health-v1", "GET", "/health", None),
    ("health-root", "GET", "/../health", None),
    ("org", "GET", "/organization", None),
    ("batches", "GET", "/batches", None),
    ("files", "GET", "/files", None),
    ("bogus-path", "GET", "/definitely-not-real", None),
    ("bogus-path-post", "POST", "/definitely-not-real", {"a": 1}),
]


def hit(name, method, path, body):
    rec = {"name": name, "method": method, "path": path,
           "ts": dt.datetime.now(dt.timezone.utc).isoformat()}
    data = json.dumps(body).encode() if body is not None else None
    headers = {}
    if data is not None:
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(BASE + path, data=data, headers=headers,
                                 method=method)
    add_surrogate_to_request(req, CRED, allowed_hosts=HOSTS)
    t0 = time.monotonic()
    try:
        with urllib.request.urlopen(req, timeout=TO) as resp:
            rec["ttfb_ms"] = round((time.monotonic() - t0) * 1000, 1)
            rec["status"] = resp.status
            rec["headers"] = {k.lower(): v for k, v in resp.headers.items()}
            raw = resp.read()
            rec["outcome"] = "ok"
    except urllib.error.HTTPError as e:
        rec["ttfb_ms"] = round((time.monotonic() - t0) * 1000, 1)
        rec["status"] = e.code
        try:
            rec["headers"] = {k.lower(): v for k, v in e.headers.items()}
        except Exception:
            rec["headers"] = {}
        try:
            raw = e.read()
        except Exception:
            raw = b""
        rec["outcome"] = "http_error"
    except Exception as e:
        rec["total_ms"] = round((time.monotonic() - t0) * 1000, 1)
        rec["outcome"] = f"exception:{type(e).__name__}"
        rec["exc"] = str(e)[:200]
        return rec
    rec["total_ms"] = round((time.monotonic() - t0) * 1000, 1)
    rec["body_len"] = len(raw)
    rec["body"] = raw[:BODY_CAP].decode("utf-8", errors="replace")
    return rec


def main():
    out = []
    for name, method, path, body in TARGETS:
        rec = hit(name, method, path, body)
        out.append(rec)
        hdrs = rec.get("headers", {})
        interesting = {k: v[:80] for k, v in hdrs.items()
                       if k in ("deprecation", "nvcf-status", "nvcf-reqid",
                                "content-type", "x-request-id")}
        print(f"{rec['status']} {name:22s} {method:4s} {path:55s} "
              f"ttfb={rec.get('ttfb_ms')}ms body={rec.get('body_len')} "
              f"{json.dumps(interesting)[:160]}", flush=True)
        b = rec.get("body", "")[:220].replace("\n", " ")
        if b:
            print(f"    body: {b}", flush=True)
    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d")
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        f"fuzz_endpoints_{stamp}.json")
    json.dump(out, open(path, "w"), indent=2)
    print(f"\nwrote {path} ({len(out)} records)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
