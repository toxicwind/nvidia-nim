#!/usr/bin/env python3
"""rank.py — rank NVIDIA NIM models per task; output feeds nim.py.

Curated September 2026 snapshot of the build.nvidia.com catalog. Scores
are heuristics (quality/speed/context/tool-use), not benchmarks — verify
a model id with `nim.py models --format ids` before scripting it.

Usage:
  rank.py --task tldr [--top 3] [--format json|table|id]
  rank.py --list-tasks
  rank.py --models   # dump the raw table
"""
from __future__ import annotations

import argparse
import json

# quality, speed, context, tools, vision: 1..10 heuristic scores.
# IDs verified live against /v1/models on 2026-09-14; `avail` records what a
# real completion call returned that day: verified (answered), listed (in
# /v1/models but 404 for this account/key), flaky (timeouts), eol (410 dead).
# The catalog drifts; re-verify with `nim.py models --format ids` + a tiny
# chat before scripting new ids.
MODELS = [
    {
        "id": "nvidia/nemotron-3-super-120b-a12b",
        "params": "120B/12B MoE", "ctx": "1M",
        "quality": 9, "speed": 6, "context": 10, "tools": 7, "vision": 0,
        "avail": "verified",
        "notes": "VERIFIED working 2026-09-14. High-accuracy reasoning, multi-agent workflows. Default pick.",
    },
    {
        "id": "nvidia/nemotron-3-ultra-550b-a55b",
        "params": "550B/55B MoE", "ctx": "1M",
        "quality": 10, "speed": 3, "context": 10, "tools": 7, "vision": 0,
        "avail": "listed",
        "notes": "Ultra: SOTA accuracy, multi-GPU class; slow. Untested on this key.",
    },
    {
        "id": "nvidia/nemotron-3-nano-omni-30b-a3b-reasoning",
        "params": "30B/3.2B MoE", "ctx": "1M",
        "quality": 8, "speed": 7, "context": 10, "tools": 6, "vision": 1,
        "avail": "listed",
        "notes": "Omni reasoning Nano; toggleable thinking, multimodal. Untested.",
    },
    {
        "id": "nvidia/llama-3.1-nemotron-70b-instruct",
        "params": "70B", "ctx": "128K",
        "quality": 9, "speed": 5, "context": 7, "tools": 7, "vision": 0,
        "avail": "listed",
        "notes": "Reliable large instruct. Untested on this key.",
    },
    {
        "id": "moonshotai/kimi-k2.6",
        "params": "large", "ctx": "256K",
        "quality": 9, "speed": 5, "context": 9, "tools": 8, "vision": 0,
        "avail": "listed",
        "notes": "Agentic long-context. Untested.",
    },
    {
        "id": "deepseek-ai/deepseek-v4-pro-0813",
        "params": "large", "ctx": "128K",
        "quality": 9, "speed": 4, "context": 7, "tools": 6, "vision": 0,
        "avail": "listed",
        "notes": "Pro variant: max reasoning, slower. Untested.",
    },
    {
        "id": "nvidia/llama-3.1-nemotron-51b-instruct",
        "params": "51B", "ctx": "128K",
        "quality": 8, "speed": 6, "context": 7, "tools": 7, "vision": 0,
        "avail": "listed",
        "notes": "NAS-compressed 70B; single-H100 class. Untested.",
    },
    {
        "id": "mistralai/mistral-large-2-instruct",
        "params": "large", "ctx": "128K",
        "quality": 8, "speed": 5, "context": 7, "tools": 7, "vision": 0,
        "avail": "listed",
        "notes": "Strong general instruct. Untested.",
    },
    {
        "id": "z-ai/glm-5.3-flash",
        "params": "large", "ctx": "128K",
        "quality": 7, "speed": 9, "context": 7, "tools": 7, "vision": 0,
        "avail": "listed",
        "notes": "Fast GLM flash; good multilingual. Untested.",
    },
    {
        "id": "openai/gpt-oss-20b",
        "params": "20B", "ctx": "128K",
        "quality": 7, "speed": 8, "context": 7, "tools": 8, "vision": 0,
        "avail": "listed",
        "notes": "Open-weights GPT; solid tool use. Untested.",
    },
    {
        "id": "google/gemma-4-31b-it",
        "params": "31B", "ctx": "128K",
        "quality": 7, "speed": 8, "context": 7, "tools": 5, "vision": 0,
        "avail": "listed",
        "notes": "Mid-size Gemma; efficient. Untested.",
    },
    {
        "id": "nvidia/nemotron-nano-3-30b-a3b",
        "params": "30B/3.2B MoE", "ctx": "1M",
        "quality": 7, "speed": 10, "context": 10, "tools": 6, "vision": 0,
        "avail": "listed",
        "notes": "404 for this account despite being listed; may work on other keys.",
    },
    {
        "id": "nvidia/mistral-nemo-minitron-8b-8k-instruct",
        "params": "8B", "ctx": "8K",
        "quality": 6, "speed": 9, "context": 4, "tools": 5, "vision": 0,
        "avail": "listed",
        "notes": "Small fast instruct; short inputs. Untested.",
    },
    {
        "id": "google/gemma-3-4b-it",
        "params": "4B", "ctx": "128K",
        "quality": 5, "speed": 10, "context": 7, "tools": 4, "vision": 0,
        "avail": "listed",
        "notes": "Tiny and fast; trivial tasks only. Untested.",
    },
    {
        "id": "nvidia/nemotron-3.5-lightning-30b-a3b",
        "params": "30B/3.2B MoE", "ctx": "1M",
        "quality": 7, "speed": 10, "context": 10, "tools": 6, "vision": 0,
        "avail": "flaky",
        "notes": "Speed-tuned; timed out on probe 2026-09-14 (cold start?).",
    },
    {
        "id": "moonshotai/kimi-k3",
        "params": "large", "ctx": "256K",
        "quality": 9, "speed": 5, "context": 9, "tools": 9, "vision": 0,
        "avail": "flaky",
        "notes": "Agentic, strong tool use; timed out on probe 2026-09-14.",
    },
    {
        "id": "deepseek-ai/deepseek-v4-flash-0731",
        "params": "large", "ctx": "128K",
        "quality": 8, "speed": 8, "context": 7, "tools": 6, "vision": 0,
        "avail": "flaky",
        "notes": "Flash variant; answered once with null content, then timed out.",
    },
    {
        "id": "nvidia/llama-3.1-nemotron-ultra-253b-v1",
        "params": "253B", "ctx": "128K",
        "quality": 10, "speed": 3, "context": 7, "tools": 7, "vision": 0,
        "avail": "listed",
        "notes": "404 for this account despite being listed.",
    },
    {
        "id": "nvidia/nemotron-3-nano-30b-a3b",
        "params": "30B/3.2B MoE", "ctx": "1M",
        "quality": 7, "speed": 10, "context": 10, "tools": 6, "vision": 0,
        "avail": "eol",
        "notes": "DEAD: HTTP 410, reached end of life. Kept as a warning.",
    },
]

# task -> weights over (quality, speed, context, tools)
TASKS = {
    "tldr": {
        "weights": {"quality": 0.45, "speed": 0.30, "context": 0.15, "tools": 0.10},
        "blurb": "abstractive paper summaries (1-2 sentences)",
    },
    "rerank": {
        "weights": {"quality": 0.35, "speed": 0.45, "context": 0.10, "tools": 0.10},
        "blurb": "score/rank a list of papers per query",
    },
    "chat": {
        "weights": {"quality": 0.50, "speed": 0.25, "context": 0.15, "tools": 0.10},
        "blurb": "general chat / Q&A",
    },
    "reasoning": {
        "weights": {"quality": 0.65, "speed": 0.10, "context": 0.15, "tools": 0.10},
        "blurb": "hard reasoning, analysis, proofs",
    },
    "agent": {
        "weights": {"quality": 0.40, "speed": 0.20, "context": 0.15, "tools": 0.25},
        "blurb": "agentic tool-calling loops",
    },
    "longctx": {
        "weights": {"quality": 0.30, "speed": 0.20, "context": 0.45, "tools": 0.05},
        "blurb": "very long documents",
    },
    "fast": {
        "weights": {"quality": 0.20, "speed": 0.65, "context": 0.10, "tools": 0.05},
        "blurb": "bulk / latency-sensitive calls",
    },
}


AVAIL_FACTOR = {"verified": 1.0, "listed": 0.7, "flaky": 0.5, "eol": 0.0}


def score(model: dict, task: str) -> float:
    w = TASKS[task]["weights"]
    base = (
        model["quality"] * w["quality"]
        + model["speed"] * w["speed"]
        + model["context"] * w["context"]
        + model["tools"] * w["tools"]
    )
    return round(base * AVAIL_FACTOR.get(model.get("avail", "listed"), 0.7), 2)


def rank(task: str, top: int) -> list[dict]:
    ranked = sorted(
        ({**m, "score": score(m, task)} for m in MODELS),
        key=lambda m: m["score"],
        reverse=True,
    )
    return ranked[:top]


def main() -> int:
    ap = argparse.ArgumentParser(prog="rank.py", description=__doc__)
    ap.add_argument("--task", default="tldr", choices=sorted(TASKS),
                    help="task to rank models for")
    ap.add_argument("--top", type=int, default=3)
    ap.add_argument("--format", choices=["json", "table", "id"], default="table")
    ap.add_argument("--list-tasks", action="store_true")
    ap.add_argument("--models", action="store_true", help="dump raw model table")
    args = ap.parse_args()

    if args.list_tasks:
        for t, spec in sorted(TASKS.items()):
            print(f"{t:10s} {spec['blurb']}")
        return 0
    if args.models:
        print(json.dumps(MODELS, indent=2))
        return 0

    ranked = rank(args.task, args.top)
    if args.format == "id":
        print(ranked[0]["id"])
    elif args.format == "json":
        print(json.dumps(
            {"task": args.task, "ranking": ranked}, indent=2
        ))
    else:
        print(f"task: {args.task} — {TASKS[args.task]['blurb']}\n")
        for i, m in enumerate(ranked, 1):
            print(f"{i}. {m['id']}  (score {m['score']})")
            print(f"   {m['params']}, ctx {m['ctx']} — {m['notes']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
