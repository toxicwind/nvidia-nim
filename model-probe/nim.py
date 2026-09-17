#!/usr/bin/env python3
"""nim.py — NVIDIA NIM completions loader.

Calls the hosted NVIDIA NIM API (https://integrate.api.nvidia.com/v1),
an OpenAI-compatible completions endpoint. Auth goes through the Secure
Vault via the dynamic credential surrogate (custom.nvidia); the raw API
key is never readable, printable, or stored in files.

Commands:
  models                  list model ids available on the NIM endpoint
  chat  --model ID PROMPT run one chat completion
  ping                    tiny health check (models endpoint)

The CLI runs on this skill's external venv:
  ~/workspace/skills/nvidia-nim-loader/.venv/bin/python
"""
from __future__ import annotations

import argparse
import json
import sys
import urllib.request

from auth import (
    DynamicCredentialError,
    add_surrogate_to_request,
    read_response_body,
)

BASE = "https://integrate.api.nvidia.com/v1"
CRED = "custom.nvidia"
HOSTS = ["integrate.api.nvidia.com"]


def _authed_request(url: str, payload: dict | None = None) -> urllib.request.Request:
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST" if data else "GET",
    )
    add_surrogate_to_request(req, CRED, allowed_hosts=HOSTS)
    return req


def _call(url: str, payload: dict | None, timeout: float) -> dict:
    try:
        req = _authed_request(url, payload)
    except DynamicCredentialError as exc:
        return {
            "ok": False,
            "error": "no_nvidia_credential",
            "detail": (
                f"{exc}. Store an NVIDIA API key (build.nvidia.com, starts "
                "with nvapi-) in the Secure Vault as custom.nvidia, then retry."
            ),
        }
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return {"ok": True, "data": json.loads(read_response_body(resp))}
    except urllib.error.HTTPError as exc:  # type: ignore[attr-defined]
        try:
            detail = read_response_body(exc).decode()[:500]
        except Exception:
            detail = str(exc)
        return {"ok": False, "error": f"http_{exc.code}", "detail": detail}
    except Exception as exc:
        return {"ok": False, "error": "request_failed", "detail": str(exc)[:500]}


def cmd_models(args: argparse.Namespace) -> int:
    res = _call(f"{BASE}/models", None, args.timeout)
    if not res["ok"]:
        print(json.dumps(res, indent=2))
        return 1
    models = res["data"].get("data", [])
    if args.format == "ids":
        for m in models:
            print(m.get("id"))
    else:
        print(json.dumps(res["data"], indent=2))
    return 0


def cmd_ping(args: argparse.Namespace) -> int:
    res = _call(f"{BASE}/models", None, args.timeout)
    print(json.dumps(
        {"ok": res["ok"], "error": res.get("error")}, indent=2
    ))
    return 0 if res["ok"] else 1


def cmd_chat(args: argparse.Namespace) -> int:
    prompt = args.prompt
    if prompt == "-" or (not prompt and not sys.stdin.isatty()):
        prompt = sys.stdin.read().strip()
    if not prompt:
        print(json.dumps({"ok": False, "error": "empty_prompt"}))
        return 1
    messages = []
    if args.system:
        messages.append({"role": "system", "content": args.system})
    messages.append({"role": "user", "content": prompt})
    payload = {
        "model": args.model,
        "messages": messages,
        "temperature": args.temperature,
        "max_tokens": args.max_tokens,
    }
    res = _call(f"{BASE}/chat/completions", payload, args.timeout)
    if not res["ok"]:
        print(json.dumps(res, indent=2))
        return 1
    if args.format == "text":
        try:
            msg = res["data"]["choices"][0]["message"]
            text = msg.get("content") or msg.get("reasoning_content")
            if text is None:
                raise KeyError("no content")
            print(text)
        except (KeyError, IndexError):
            print(json.dumps(res["data"], indent=2))
            return 1
    else:
        print(json.dumps(res["data"], indent=2))
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(prog="nim.py", description=__doc__)
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("models", help="list model ids on the NIM endpoint")
    p.add_argument("--timeout", type=float, default=20)
    p.add_argument("--format", choices=["json", "ids"], default="json")

    p = sub.add_parser("ping", help="health check against /v1/models")
    p.add_argument("--timeout", type=float, default=10)

    p = sub.add_parser("chat", help="run one chat completion")
    p.add_argument("--model", required=True, help="NIM model id, e.g. nvidia/llama-3.1-nemotron-nano-8b-v1")
    p.add_argument("prompt", nargs="?", default=None, help="prompt text; '-' or empty reads stdin")
    p.add_argument("--system", default=None, help="system prompt")
    p.add_argument("--temperature", type=float, default=0.2)
    p.add_argument("--max-tokens", type=int, default=512)
    p.add_argument("--timeout", type=float, default=90)
    p.add_argument("--format", choices=["json", "text"], default="json")

    args = ap.parse_args()
    if args.cmd == "models":
        return cmd_models(args)
    if args.cmd == "ping":
        return cmd_ping(args)
    return cmd_chat(args)


if __name__ == "__main__":
    raise SystemExit(main())
