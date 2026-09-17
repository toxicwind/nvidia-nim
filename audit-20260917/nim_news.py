#!/usr/bin/env python3
"""Fetch NVIDIA NIM past-week news via Exa through shep gateway -> parquet."""
import json
import sys
import time

import pandas as pd

sys.path.insert(0, "/home/toxic")
from exa_gw import session, exa_call  # noqa: E402

QUERIES = [
    "NVIDIA NIM new model release September 2026",
    "new model added build.nvidia.com NIM model card",
    "NVIDIA NIM model announcement this week",
    "NVIDIA AI Enterprise new foundation model NIM September 2026",
]

OUT = "/home/toxic/nim-news-20260917.parquet"


def main():
    sid = session()
    rows = []
    for q in QUERIES:
        raw = exa_call(sid, "web_search_exa",
                       {"query": q, "numResults": 10})
        rows.append({"query": q, "fetched_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
                     "raw": raw})
        print(f"query done: {q[:50]} ({len(raw)} chars)")
    df = pd.DataFrame(rows)
    df.to_parquet(OUT, index=False)
    print(f"saved {len(df)} rows -> {OUT}")


if __name__ == "__main__":
    main()
