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
import sys
import time
import urllib.request

import os
from auth import add_surrogate_to_request

BASE = "https://integrate.api.nvidia.com/v1"
CRED = "custom.nvidia"
HOSTS = ["integrate.api.nvidia.com"]
_HERE = os.path.dirname(os.path.abspath(__file__))
AUDIT = os.path.join(_HERE, "probe_audit.jsonl")
RANK_PY = os.path.join(_HERE, "rank.py")


def tiny_completion(model, timeout, max_tokens=3, stream=False):
    """Return (ok, status_or_err, latency_ms, detail, ttft_ms)."""
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
            if not stream:
                body = resp.read().decode()
                d = json.loads(body)
                content = d["choices"][0]["message"].get("content")
                dt_ms = (time.monotonic() - t0) * 1000
                return True, resp.status, dt_ms, (content or "")[:60], None
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
                        dt_ms = (time.monotonic() - t0) * 1000
                        return True, resp.status, dt_ms, "stream-chunk-ok", ttft
            dt_ms = (time.monotonic() - t0) * 1000
            return True, resp.status, dt_ms, "stream-empty", ttft
    except urllib.error.HTTPError as e:
        dt_ms = (time.monotonic() - t0) * 1000
        try:
            detail = e.read().decode()[:160]
        except Exception:
            detail = ""
        return False, e.code, dt_ms, detail, ttft
    except Exception as e:
        dt_ms = (time.monotonic() - t0) * 1000
        return False, type(e).__name__, dt_ms, str(e)[:160], ttft


def diagnose(model, t_a=12, t_c=60):
    """Run the ladder. Returns a dict with verdict + evidence."""
    rec = {"model": model, "ts": dt.datetime.now(dt.timezone.utc).isoformat()}
    ok, status, lat, detail, _ = tiny_completion(model, t_a)
    rec["phase_a"] = {"ok": ok, "status": status, "lat_ms": round(lat, 1),
                      "detail": detail[:120]}
    if ok:
        verdict = "alive-fast" if lat < 5000 else "alive"
        # Phase B: streaming check
        ok2, s2, lat2, d2, ttft = tiny_completion(model, 25, 10, stream=True)
        rec["phase_b"] = {"ok": ok2, "status": s2, "lat_ms": round(lat2, 1),
                          "ttft_ms": round(ttft, 1) if ttft else None,
                          "detail": str(d2)[:80]}
        if not ok2 and s2 in ("timeout", "TimeoutError"):
            verdict = "streaming-stall"
        elif not ok2:
            verdict = "alive-nostream-err"
        rec["verdict"] = verdict
    elif status == 404:
        rec["verdict"] = "dead-404-gated"
    elif status == 410:
        rec["verdict"] = "dead-410-eol"
    elif status == 429:
        rec["verdict"] = "rate-limited-429"
    elif status in ("timeout", "TimeoutError", "socket.timeout", "URLError"):
        # Phase C: ambiguous timeout -> one slow retry to separate
        # cold-start latency from actually-dead
        ok3, s3, lat3, d3, _ = tiny_completion(model, t_c)
        rec["phase_c"] = {"ok": ok3, "status": s3, "lat_ms": round(lat3, 1),
                          "detail": str(d3)[:120]}
        rec["verdict"] = "alive-slow-coldstart" if ok3 else "flaky-timeout"
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
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    models = load_catalog_models() if args.all else load_ranked_models()
    print(f"probing {len(models)} models (fail-fast ladder)\n", flush=True)
    results = []
    with open(AUDIT, "a") as audit:
        for i, m in enumerate(models):
            rec = diagnose(m, args.timeout_a, args.timeout_c)
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
    if args.out:
        json.dump(results, open(args.out, "w"), indent=2)
        print(f"\nwrote {args.out}")
    print(f"audit appended to {AUDIT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
