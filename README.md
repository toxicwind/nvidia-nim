# NVIDIA NIM is lying to you — we probed the models one by one

![last probed](https://img.shields.io/badge/last%20probed-2026--09--14-blue)
![models probed](https://img.shields.io/badge/models%20probed-19-orange)
![actually usable](https://img.shields.io/badge/actually%20usable-5-brightgreen)
![license](https://img.shields.io/badge/license-MIT-green)

**`GET /v1/models` on NVIDIA's NIM API returns 82 shiny model IDs. We ran a fail-fast diagnostic ladder against 19 of them, one by one. Only 5 actually answer.** The rest are ghosts: 404-gated, end-of-lifed, 503'd, streaming black holes, or cold-start zombies.

If you build on NIM, stop trusting the catalog. Run the probe.

## Contents

- [The headline numbers](#the-headline-numbers)
- [Verdict table](#verdict-table)
- [Per-model deep dives](#per-model-deep-dives)
- [The catalog is an unreliable narrator](#the-catalog-is-an-unreliable-narrator)
- [Why the catalog lies (root cause)](#why-the-catalog-lies-root-cause)
- [Independent confirmation](#independent-confirmation)
- [The diagnostic ladder](#the-diagnostic-ladder)
- [Reproduce it](#reproduce-it)
- [The tools](#the-tools)
- [Raw data](#raw-data)
- [License](#license)

## The headline numbers

Probed 2026-09-14 against `https://integrate.api.nvidia.com/v1` (free build.nvidia.com key):

| verdict | count | meaning |
|---|---|---|
| `alive-fast` | 4 | answers in under ~3s, streaming works |
| `alive-slow-coldstart` | 1 | answers, but needs a 60s cold start |
| `streaming-stall` | 1 | answers non-streaming, **hangs on SSE streaming** |
| `flaky-timeout` | 3 | timed out at 12s *and* 60s — effectively dead |
| `error-other` | 1 | instant HTTP 503 — routed, but no backend |
| `dead-404-gated` | 8 | listed, but "not found for account" |
| `dead-410-eol` | 1 | end-of-lifed — **still listed in the catalog** |

## Verdict table

| model | verdict | probe | streaming TTFT | deep dive |
|---|---|---|---|---|
| `nvidia/nemotron-3-super-120b-a12b` | ✅ alive-fast | 815ms | 779ms | [notes](#nvidianemotron-3-super-120b-a12b) |
| `deepseek-ai/deepseek-v4-pro-0813` | ✅ alive-fast | 2717ms | 2313ms | [notes](#deepseek-aideepseek-v4-pro-0813) |
| `z-ai/glm-5.3-flash` | ✅ alive-fast | 583ms | 1155ms | [notes](#z-aiglm-53-flash) |
| `openai/gpt-oss-20b` | ✅ alive-fast | 1883ms | 682ms | [notes](#openaigpt-oss-20b) |
| `google/gemma-4-31b-it` | ⚠️ alive-slow-coldstart | 12s timeout → 60s OK | — | [notes](#googlegemma-4-31b-it) |
| `deepseek-ai/deepseek-v4-flash-0731` | ⚠️ streaming-stall | 1109ms non-streaming | **hangs** | [notes](#deepseek-aideepseek-v4-flash-0731) |
| `nvidia/nemotron-3-ultra-550b-a55b` | ❌ flaky-timeout | 12s + 60s timeout | — | [notes](#nvidianemotron-3-ultra-550b-a55b) |
| `nvidia/nemotron-3.5-lightning-30b-a3b` | ❌ flaky-timeout | 12s + 60s timeout | — | [notes](#nvidianemotron-35-lightning-30b-a3b) |
| `moonshotai/kimi-k3` | ❌ flaky-timeout | 12s + 60s timeout | — | [notes](#moonshotaikimi-k3) |
| `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning` | ❌ 503 | 667ms | — | [notes](#nvidianemotron-3-nano-omni-30b-a3b-reasoning) |
| `nvidia/llama-3.1-nemotron-70b-instruct` | ❌ 404-gated | 376ms | — | [notes](#nvidiallama-31-nemotron-70b-instruct) |
| `nvidia/llama-3.1-nemotron-51b-instruct` | ❌ 404-gated | 322ms | — | [notes](#nvidiallama-31-nemotron-51b-instruct) |
| `nvidia/llama-3.1-nemotron-ultra-253b-v1` | ❌ 404-gated | 636ms | — | [notes](#nvidiallama-31-nemotron-ultra-253b-v1) |
| `nvidia/nemotron-nano-3-30b-a3b` | ❌ 404-gated | 561ms | — | [notes](#nvidianemotron-nano-3-30b-a3b) |
| `nvidia/mistral-nemo-minitron-8b-8k-instruct` | ❌ 404-gated | 386ms | — | [notes](#nvidiamistral-nemo-minitron-8b-8k-instruct) |
| `mistralai/mistral-large-2-instruct` | ❌ 404-gated | 350ms | — | [notes](#mistralaimistral-large-2-instruct) |
| `moonshotai/kimi-k2.6` | ❌ 404-gated | 438ms | — | [notes](#moonshotaikimi-k26) |
| `google/gemma-3-4b-it` | ❌ 404-gated | 376ms | — | [notes](#googlegemma-3-4b-it) |
| `nvidia/nemotron-3-nano-30b-a3b` | ☠️ 410 EOL | 309ms | — | [notes](#nvidianemotron-3-nano-30b-a3b) |

## Per-model deep dives

#### nvidia/nemotron-3-super-120b-a12b

**✅ alive-fast — the workhorse.** 815ms probe, 779ms streaming TTFT. The only model that completed our complex multi-hop tool-use benchmark (look up 3 papers → compute cites/year → ranked JSON) — though it was inconsistent run to run (PASS once, FAIL once), so treat its tool-calling as moody. Default pick for anything serious on the free tier.

#### deepseek-ai/deepseek-v4-pro-0813

**✅ alive-fast, with reasoning-model tax.** 2717ms probe, 2313ms TTFT. Earlier in the day it answered once with a null content body and then timed out — flaky under load. Use when you want DeepSeek reasoning and can tolerate slow starts.

#### z-ai/glm-5.3-flash

**✅ alive-fast — the latency pick.** 583ms probe, fastest of the usable set. If you need quick completions and don't need frontier reasoning, this is the one.

#### openai/gpt-oss-20b

**✅ alive-fast — best time-to-first-token.** 1883ms probe but only 682ms streaming TTFT: it starts talking fast, then thinks a while. Good for interactive streaming UX.

#### google/gemma-4-31b-it

**⚠️ alive-slow-coldstart — the cold-start proof.** Timed out at 12s, answered on the 60s retry. This is exactly why the ladder has Phase C: a naive probe would have filed it as dead. Usable only if your timeout budget exceeds ~60s.

#### deepseek-ai/deepseek-v4-flash-0731

**⚠️ streaming-stall — the smoking gun.** Non-streaming: HTTP 200 in 1109ms. Streaming SSE: hangs past 25s. Two different serving paths, only one works. Since nearly every production stack streams, this model is **effectively unusable** despite being "alive".

#### nvidia/nemotron-3-ultra-550b-a55b

**❌ flaky-timeout.** 12s timeout, then 60s timeout. The 550B flagship never picks up. Either permanently cold, deprovisioned without updating the catalog, or hanging infra. Treat as dead until proven otherwise.

#### nvidia/nemotron-3.5-lightning-30b-a3b

**❌ flaky-timeout.** Ironic for a model named "lightning". Same double-timeout pattern as the 550B.

#### moonshotai/kimi-k3

**❌ flaky-timeout.** Same story. The Kimi models look great on the catalog page; neither answers on this tier.

#### nvidia/nemotron-3-nano-omni-30b-a3b-reasoning

**❌ HTTP 503 in 667ms.** Different from a 404: the router *knows* this model, it just has no backend capacity for it right now. May come back; not usable today.

#### nvidia/llama-3.1-nemotron-70b-instruct

**❌ 404-gated in 376ms.** Listed in `/v1/models`; the API replies "not found for account". Per-account entitlement gating — the catalog is a superset, not your allowance.

#### nvidia/llama-3.1-nemotron-51b-instruct

**❌ 404-gated in 322ms.** Same gating story.

#### nvidia/llama-3.1-nemotron-ultra-253b-v1

**❌ 404-gated in 636ms.** Same gating story. The 253B "SOTA reasoning" model is catalog decoration on the free tier.

#### nvidia/nemotron-nano-3-30b-a3b

**❌ 404-gated in 561ms.** The previous-gen Nano. Listed, gated.

#### nvidia/mistral-nemo-minitron-8b-8k-instruct

**❌ 404-gated in 386ms.** Even the tiny 8B is gated. Gating is not about size.

#### mistralai/mistral-large-2-instruct

**❌ 404-gated in 350ms.** Same.

#### moonshotai/kimi-k2.6

**❌ 404-gated in 438ms.** Same.

#### google/gemma-3-4b-it

**❌ 404-gated in 376ms.** Same.

#### nvidia/nemotron-3-nano-30b-a3b

**☠️ 410 Gone in 309ms — end of life, still listed.** The catalog doesn't even prune the dead. If you hardcoded this ID from an old tutorial, it will never work again.

## The catalog is an unreliable narrator

Four distinct ways `/v1/models` misleads you, all observed in one afternoon:

1. **Listed but gated (8/19).** HTTP 404 "not found for account" in ~350ms. The endpoint returns the global catalog, not your entitlement. There is no per-account availability endpoint — you have to probe.
2. **Listed but dead (1/19).** HTTP 410 end-of-life. No pruning.
3. **Listed but unserved (1/19).** HTTP 503 — routed, no capacity.
4. **Alive but half-broken (1/19).** Non-streaming works, SSE streaming hangs. The two paths are served differently; test the one you actually use.

Plus the latency dimension: one model needed a 60s cold start, three never answered at all. A single-timeout probe conflates all of these into "failed". The ladder below exists to separate them.

## Why the catalog lies (root cause)

`GET /v1/models` returns the **global marketing superset** (~100 models), not your entitlement. Actual inference is gated per-account by a **"Public API Endpoints"** permission scope on your build.nvidia.com org. NVIDIA's own developer forums document this extensively (Jul-Sep 2026):

- [Public API Endpoints scope missing: Llama/Gemma work, Kimi/DeepSeek/Qwen/Nemotron all 404](https://forums.developer.nvidia.com/t/public-api-endpoints-scope-missing-on-personal-org-llama-gemma-work-kimi-deepseek-qwen-nemotron-all-404/378043) — same key, catalog returns 200, playground works, but chat completions 404 on partner models. A free "public" subset (Llama, Gemma, GPT-OSS) keeps working; Kimi, DeepSeek, Qwen, Nemotron-3, Mistral require the scope. Described as an auto-provisioning gap on newly-created personal orgs.
- [Newer NIM models hang indefinitely or 404](https://forums.developer.nvidia.com/t/newer-nim-models-kimi-k2-6-deepseek-v4-pro-hang-indefinitely-or-404-possible-missing-public-api-endpoints-permission/377777) — the latency-vs-404 distinction: some gated models 404 immediately, others hang with zero bytes until client timeout. That is exactly our `flaky-timeout` verdict, explained.
- [Per-model entitlements, not all-or-nothing](https://forums.developer.nvidia.com/t/function-not-found-for-account-moonshotai-kimi-k2-6-and-deepseek-ai-deepseek-v4-pro-0813-404/382736) — one user had `ultra-550b` answering while Kimi/DeepSeek 404'd. Gating is per-model.

So the error `Function '<uuid>': Not found for account '<id>'` is not a bug — it is the entitlement check failing. **If you want broader access, the documented fix is asking NVIDIA support to enable the "Public API Endpoints" scope on your org** (the forum threads above are the request template).

## The diagnostic ladder

`probe.py` runs three phases per model — fail fast, diagnose deep:

- **Phase A** — tiny non-streaming completion (`max_tokens=3`, 12s timeout). 200 → alive; 404 → gated; 410 → EOL; 429 → back off 60s; timeout → ambiguous, go to C.
- **Phase B** — streaming probe: open SSE, close after the first content chunk (25s timeout). Records time-to-first-token. Catches streaming stalls on models whose non-streaming path works.
- **Phase C** — slow retry (60s), only if Phase A timed out. Success → `alive-slow-coldstart` (latency, not death). Failure → `flaky-timeout`.

Every model appends one JSON line to `probe_audit.jsonl`: verdict, phase timings, error detail. Fail fast by default, diagnose on ambiguity.

## Reproduce it

```bash
git clone https://github.com/toxicwind/nvidia-nim-model-probe
cd nvidia-nim-model-probe
export NVIDIA_API_KEY=...   # free key from https://build.nvidia.com
python3 probe.py            # probes the 19-model table
python3 probe.py --all      # probes every id in the live /v1/models catalog
```

## The tools

- **`probe.py`** — the fail-fast diagnostic ladder above. `--all` hits the full catalog.
- **`bench.py`** — live streaming tool-use benchmark: same complex multi-hop task (paper lookup → cites/year math → ranked JSON) against top-ranked candidates, ranked on observed success, tool-call validity, turns, TTFT, tokens/sec. Also parses textual pseudo tool calls (`<function=name>` style) some NIM models emit instead of native `tool_calls`.
- **`nim.py`** — minimal NIM client: `models`, `chat`, `ping` over the OpenAI-compatible API.
- **`rank.py`** — heuristic model ranking table (Sept 2026) with availability weighting; `--format id` feeds the winner straight into `nim.py`.

## Independent confirmation

We are not the only ones who stopped trusting the catalog. [aviclaw01/nvclaude](https://github.com/aviclaw01/nvclaude) (updated 2026-09-14) independently documents the same core finding: *"The public `/v1/models` list is not account-scoped: several ids 404 with 'Function … not found for account'"* — with an overlapping 404 list (`nemotron-nano-3-30b`, `llama-3.1-nemotron-ultra-253b-v1`, `llama-3.1-nemotron-70b-instruct`). Their live probes also confirm the deepseek latency pathology (v4-pro first-token in the hundreds of seconds, effectively unusable synchronously).

Related tooling worth knowing about:

- [sherman-yang/nvidia-model-info](https://github.com/sherman-yang/nvidia-model-info) — the most thorough probe harness found: paced availability ladder, streaming probes, capability probes (structured output, forced/parallel tool calls, vision), and a failure taxonomy.
- [Jontte6/nim-to-openai-proxy](https://github.com/Jontte6/nim-to-openai-proxy) — operational availability routing: live re-validation plus per-model cooldown after failures.
- [xRyul/pi-nvidia-nim](https://github.com/xRyul/pi-nvidia-nim) — NIM provider extension for a coding agent; reference for coping with the model list in production.

## Raw data

- [`data/probe_results_2026-09-14.json`](data/probe_results_2026-09-14.json) — full per-model ladder records (account IDs redacted).
- [`data/probe_audit.jsonl`](data/probe_audit.jsonl) — the append-only audit log, one line per probe.

## License

MIT. If this saved you an afternoon of 404s, a star is the cheapest thanks there is.
