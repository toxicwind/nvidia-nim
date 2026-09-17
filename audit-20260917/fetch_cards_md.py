#!/usr/bin/env python3
"""Fetch build.nvidia.com/<org>/<model>.md for all NIM models, extract release dates -> parquet."""
import re
import time

import pandas as pd
import requests

UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"}

models = pd.read_parquet("/home/hatch/workspace/nim-audit/modelcards.parquet")["model_id"].tolist()

rows = []
for i, mid in enumerate(models, 1):
    url = f"https://build.nvidia.com/{mid}.md"
    rec = {"model_id": mid, "md_url": url, "http": None,
           "release_date": None, "md_chars": 0, "fetched_at": None}
    try:
        r = requests.get(url, headers=UA, timeout=30)
        rec["http"] = r.status_code
        rec["fetched_at"] = time.strftime("%Y-%m-%dT%H:%M:%S")
        if r.status_code == 200:
            txt = r.text
            rec["md_chars"] = len(txt)
            m = re.search(r"\|\s*\*\*Release Date\*\*\s*\|\s*([^|]+?)\s*\|", txt)
            if m:
                rec["release_date"] = m.group(1).strip()
            open(f"/home/hatch/workspace/nim-audit/cards_md/{mid.replace('/', '__')}.md",
                 "w").write(txt)
    except Exception as e:
        rec["http"] = f"ERR {type(e).__name__}"
    rows.append(rec)
    if i % 20 == 0:
        print(f"[{i}/{len(models)}] done", flush=True)

df = pd.DataFrame(rows)
df.to_parquet("/home/hatch/workspace/nim-audit/modelcards_md.parquet", index=False)
print(f"saved {len(df)} rows; dates found: {df['release_date'].notna().sum()}")
print(df[df["release_date"].notna()][["model_id", "release_date"]].to_string(index=False))
