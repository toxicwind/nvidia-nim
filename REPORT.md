# nim-proxy forensic audit — why it "never completed"

**Date:** 2026-09-15 ~03:45 UTC · **Box:** awrawr-pc · **Auditor:** subagent 4daf6cbe
**Verdict up front:** nim-proxy itself is COMPLETE and HEALTHY. The "never completed"
is not the proxy — it's two downstream integrations that never shipped, one of which
is blocked on an explicit Chris decision.

---

## 1. What I verified working (proxy is done)

| Check | Result |
|---|---|
| Daemon live | pid 2948615, ppid = pitchfork supervisor (2947304), :8000 LISTEN |
| `/health` | 200 |
| `/` (unauth) | 401 (auth enforced, correct) |
| `/metrics` (unauth) | 401 (correct) |
| `/v1/models` with npk_ client key | **200, 81 models** — full client→proxy→NVIDIA path live |
| Upstream keys | 4× `nvapi-…` keys, enabled, 40 rpm each (160 rpm aggregate) |
| Client key wiring | `NIM_PROXY_API_KEY` in `/home/toxic/.secrets` is `npk_…` (36ch); **SHA-256 matches** the proxy's configured client key (`…47e9`). The "key never supplied" premise is STALE — it exists and matches. |
| herd.yaml nvidia provider | `baseUrl: http://127.0.0.1:8000/v1`, `keyEnv: NIM_PROXY_API_KEY` — rewire intact |
| herd.sh | sources `/home/toxic/.secrets` (lines 15–18) — key reaches herd's env |
| Docker→native migration | commit `5cfe15b70d` "feat(nim-proxy): run natively, drop docker" — deliberate, verified pre-cutover ("4 keys / 160rpm loaded, keyed auth parity") |
| All-NIM-through-proxy rewire | commits `1c5bc70752` + `4ed041edb4` — herd.yaml, herd.sh, sovereign-router, profiles/toxic/env.sh, nim-client, nim-openapi-client |
| Secrets hygiene | config.json and .secrets both 0600 |

Binary: `/home/toxic/.nim-proxy/nim-proxy` v0.6.5 (5.8 MB, 2026-09-14 13:25).

## 2. Ranked reasons it "never completed"

### #1 — Herd-integration: 3 plans produced, Chris never picked → NO execution (DECISION BLOCKER)
- Fleet channel (`/home/toxic/.shingle/directives.md:82`): Chris redirected nim-proxy
  into HERD ("likely in the completions astmatrix component"), cancelled the mesh
  monorepo move, and ordered: deliverable = DECISION doc (NIM inventory, request-path
  trace, nim-proxy vs direct latency benchmark) + **3 maximal herd-integration plans**,
  **"NO execution until he picks."**
- `.shingle/todos.md:11`: "[nim-consolidation] done - 3 lowest-latency herd-integration
  plans produced for Chris; NO execution until he picks".
- Zero `nim-proxy`/`:8000` references in `sovereign/herd/` (config.yaml, astmatrix
  README/scripts) — nothing was ever wired in. No pick ever recorded in directives.md
  after line 82.
- **Unblock:** Chris picks a plan. I did NOT execute any herd wiring — his "no
  execution until he picks" order stands and the course-correction's "decision that's
  explicitly Chris's" stop-rule covers it.

### #2 — super-ralph's "nim-proxy as claude" intention never realized
- Separate audit worker covering super-ralph itself. The proxy side is ready
  (healthy :8000, keyed auth); the consumer was never wired.

### #3 — "nim-proxy key verification" paused item (directives.md:31)
- **Completed by this audit:** hash match verified + live `/v1/models` 200. Done.

### Non-blockers (verified, not problems)
- Docker→binary migration: finished, not half-done.
- npk_ key: exists, matches. Stale premise corrected (MEMORY.md entry saying the key
  "needs npk_ client key via vault — ask Chris" is outdated; the key is in `.secrets`
  and wired).
- The mesh-monorepo move: explicitly CANCELLED by Chris, not stalled.

## 3. Security note
`/home/toxic/.nim-proxy-data/config.json` holds 4 live `nvapi-…` upstream keys in
plaintext (required by nim-proxy's design). File is 0600, root-owned by toxic. No
action taken; flagging for awareness. Keys are NOT reproduced in this report.

## 4. Timeline (sovereign repo)
- `4f24a1e294`/`5abe88d8bd` — sysd-migrate stages nim-proxy :8000 defs
- `7b8498d9b1` — nim-proxy enters pitchfork as Docker (`ghcr.io/miztertea/nim-proxy:latest`)
- `1c5bc70752` (Sep 14 14:59) — route ALL NIM traffic through nim-proxy
- `4ed041edb4` (Sep 14 15:15) — rewire remaining NIM clients
- `5cfe15b70d` — Docker → native binary cutover
- directives:82 — Chris redirects to HERD, orders decision doc + 3 plans, no execution until pick
- todos:11 — 3 plans marked done; pick never happened

## 5. What I executed (course correction: audit AND execute)
- Proved :8000 serves end-to-end (`/v1/models` 200/81 models) — not just `/health`.
- Verified client-key wiring cryptographically (SHA-256 match, key value never exposed).
- Verified daemon parentage (pitchfork supervisor child) and config state.
- No repairs were needed — the proxy is healthy. Nothing live was changed.

## 6. Still blocked — needs Chris
1. **Pick one of the 3 herd-integration plans** (produced per todos.md:11; the doc file
   itself wasn't locatable in the repos searched — may have been delivered in chat).
2. super-ralph consumer wiring (other worker's lane).
