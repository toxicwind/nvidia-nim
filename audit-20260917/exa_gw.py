#!/usr/bin/env python3
"""Exa via shep gateway (mcpproxy-go intelligent discovery)."""
import json
import sys
import urllib.request

BASE = "http://127.0.0.1:25127/mcp"


def call(payload, sid=None):
    req = urllib.request.Request(
        BASE, data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json",
                 "Accept": "application/json, text/event-stream"})
    if sid:
        req.add_header("mcp-session-id", sid)
    with urllib.request.urlopen(req, timeout=90) as r:
        body = r.read().decode().strip()
        return r.headers.get("mcp-session-id"), (json.loads(body) if body else {})


def session():
    sid, _ = call({"jsonrpc": "2.0", "id": 1, "method": "initialize",
                   "params": {"protocolVersion": "2025-06-18", "capabilities": {},
                              "clientInfo": {"name": "exa-gw", "version": "1"}}})
    call({"jsonrpc": "2.0", "method": "notifications/initialized"}, sid)
    return sid


def mcpcall(sid, tool, args, rid=3):
    _, out = call({"jsonrpc": "2.0", "id": rid, "method": "tools/call",
                   "params": {"name": tool, "arguments": args}}, sid)
    res = out.get("result", {})
    texts = [c.get("text", "") for c in res.get("content", []) if c.get("type") == "text"]
    return "\n".join(texts) or json.dumps(res)[:5000]


def exa_call(sid, tool_name, tool_args):
    """Call an exa tool via the gateway's call_tool_read (args_json format)."""
    return mcpcall(sid, "call_tool_read",
                   {"name": "exa:" + tool_name,
                    "args_json": json.dumps(tool_args),
                    "intent": {"operation_type": "read",
                               "data_sensitivity": "public",
                               "reason": "audit NVIDIA NIM model releases past week"}})


def discover(sid, query):
    return mcpcall(sid, "retrieve_tools", {"query": query})


def main():
    sid = session()
    mode = sys.argv[1]
    if mode == "discover":
        print(discover(sid, sys.argv[2])[:6000])
        return
    query = sys.argv[2]
    num = int(sys.argv[3]) if len(sys.argv) > 3 else 10
    out = exa_call(sid, "web_search_exa",
                   {"query": query, "numResults": num,
                    "startPublishedDate": "2026-09-10"})
    print(out[:30000])


def fetch_urls(sid, urls, max_chars=20000):
    out = exa_call(sid, "web_fetch_exa",
                   {"urls": urls, "maxCharacters": max_chars})
    return out


if __name__ == "__main__":
    main()
