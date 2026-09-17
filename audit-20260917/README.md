# Past-week NIM audit (2026-09-17)

Real-task audit of NVIDIA NIM model releases for 2026-09-10 → 2026-09-17,
run to prove the Exa → shep (mcpproxy-go) gateway path end-to-end.

## Method

- **Endpoint**: `GET https://integrate.api.nvidia.com/v1/models` — 82 model IDs across
  all orgs (`*/*`). The `created` field is constant (735790403) for every model,
  so it cannot date releases; card + news evidence used instead.
- **News**: Exa `web_search_exa` through the shep gateway (`call_tool_read`,
  `args_json` + `intent` convention) — 7 queries, raw results in
  `nim-news-20260917.parquet` and `nim-news-targeted.parquet`.
- **Model cards**: all 82 `build.nvidia.com/<org>/<model>` cards fetched as full
  HTML (`cards_raw/`), `.md` variants where published (`cards_md/`), release dates
  and spec tables extracted.

## Findings

- **No new model releases on the endpoint in the past week.** The 82-model list
  was stable (zero adds/removes vs the earlier same-day snapshot).
- Week's NIM news: 2026-09-10 full-stack NIM optimizations delivering 2.5x
  throughput on Nemotron 3 Ultra (NVIDIA blog + press); 2026-09-11 coverage of
  Nemotron 3.5 Lightning (released 2026-08-11, the newest dated card on file).
- Newest dated cards: Nemotron 3.5 Lightning (2026-08-11), Nemotron 3 Ultra
  (2026-06-04), Nemotron 3 Super (2026-03-11).

## Key files

| File | Contents |
|---|---|
| `nim-audit-report.parquet` | Final audit verdicts (past-week items + context rows) |
| `model_specs.parquet` / `model_catalog.parquet` | Per-model specs: context length, params, license, GPU req, release date |
| `modelcards.parquet` | 82 cards: URL, HTTP status, fetch time, extracted fields |
| `cards_raw/` | Full untruncated card HTML (82 files) |
| `exa_gw.py` | Working shep-gateway client (search + fetch) |

The consolidated per-model catalog now lives at `../models/catalog.md`
(`catalog.parquet` beside it) in this repo.
