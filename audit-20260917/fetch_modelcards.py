#!/usr/bin/env python3
"""Fetch build.nvidia.com model cards for every model on the NIM API
integrations endpoint (integrate.api.nvidia.com/v1/models, all orgs */*),
extract release metadata, save to dataframe (parquet) by default."""
import json
import re
import time
import urllib.request

import pandas as pd

API_LIST = "/tmp/nim_models.json"
OUT_DIR = "/home/hatch/workspace/nim-audit"
RAW_DIR = f"{OUT_DIR}/cards_raw"  # full untruncated HTML, one file per model
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"}


def fetch(url):
    req = urllib.request.Request(url, headers=UA)
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status, r.url, r.read().decode("utf-8", "replace")
    except Exception as e:  # noqa: BLE001
        return 0, url, f"FETCH_ERROR: {e}"


def extract(html):
    out = {}
    m = re.search(r"Model Release Date:</strong>\s*([^<]+)", html)
    out["model_release_date"] = m.group(1).strip() if m else None
    m = re.search(r"Model Developer</strong>:\s*([^<]+)", html)
    if not m:
        m = re.search(r"\*\*Model Developer\*\*:\s*([^\n<]+)", html)
    out["developer"] = m.group(1).strip() if m else None
    m = re.search(r"Number of model parameters:</strong>\s*([^<]+)", html)
    out["params"] = m.group(1).strip() if m else None
    m = re.search(r"## Release Date(.{0,600})", html, re.S)
    out["release_section"] = (m.group(1).strip()[:600] if m else None)
    return out


def main():
    ids = [m["id"] for m in json.load(open(API_LIST))["data"]]
    import os
    os.makedirs(RAW_DIR, exist_ok=True)
    rows = []
    for i, mid in enumerate(ids):
        url = f"https://build.nvidia.com/{mid}/modelcard"
        status, final, html = fetch(url)
        if status != 200:  # try underscore slug variant
            alt = f"https://build.nvidia.com/{mid.replace('.', '_')}/modelcard"
            status, final, html = fetch(alt)
            url = alt
        raw_path = None
        if status == 200:
            # full untruncated HTML saved to disk; dataframe references it
            raw_path = f"{RAW_DIR}/{mid.replace('/', '__')}.html"
            with open(raw_path, "w", encoding="utf-8") as fh:
                fh.write(html)
        row = {"model_id": mid, "card_url": url, "http": status,
               "raw_path": raw_path}
        row.update(extract(html) if status == 200 else {})
        rows.append(row)
        print(f"[{i+1}/{len(ids)}] {mid} http={status}", flush=True)
        time.sleep(0.4)
    df = pd.DataFrame(rows)
    df.to_parquet(f"{OUT_DIR}/modelcards.parquet", index=False)
    df.to_json(f"{OUT_DIR}/modelcards.json", orient="records", indent=1)
    print(f"saved {len(df)} rows -> {OUT_DIR}/modelcards.parquet")


if __name__ == "__main__":
    main()
