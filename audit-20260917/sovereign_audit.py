#!/usr/bin/env python3
"""Audit ALL files in /home/toxic/sovereign -> parquet inventory + summary.
Run on awrawr-pc. Output: /home/toxic/sovereign-audit-20260917/"""
import json
import os
import subprocess
import time

import pandas as pd

ROOT = "/home/toxic/sovereign"
OUT = "/home/toxic/sovereign-audit-20260917"


def main():
    t0 = time.time()
    os.makedirs(OUT, exist_ok=True)
    p = subprocess.run(
        ["fd", ".", ROOT, "--type", "f", "--print0", "--hidden",
         "--exclude", ".git/"],
        capture_output=True, check=True)
    paths = [x for x in p.stdout.split(b"\0") if x]
    rows = []
    for raw in paths:
        ap = raw.decode("utf-8", "replace")
        try:
            st = os.stat(ap)
        except OSError:
            continue
        rel = os.path.relpath(ap, ROOT)
        top = rel.split(os.sep)[0]
        _, ext = os.path.splitext(ap)
        rows.append({
            "path": rel,
            "top_dir": top,
            "ext": ext.lower()[:16],
            "bytes": st.st_size,
            "mtime": time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime(st.st_mtime)),
        })
    df = pd.DataFrame(rows)
    df.to_parquet(f"{OUT}/inventory.parquet", index=False)

    by_top = (df.groupby("top_dir")
                .agg(files=("path", "count"), bytes=("bytes", "sum"))
                .sort_values("bytes", ascending=False).reset_index())
    by_top.to_parquet(f"{OUT}/by_topdir.parquet", index=False)

    by_ext = (df.groupby("ext")
                .agg(files=("path", "count"), bytes=("bytes", "sum"))
                .sort_values("files", ascending=False).reset_index().head(50))
    by_ext.to_parquet(f"{OUT}/by_ext.parquet", index=False)

    recent = df[df["mtime"] >= "2026-09-10"].sort_values("mtime", ascending=False)
    recent.to_parquet(f"{OUT}/recent_7d.parquet", index=False)

    # git repos (dirs containing .git), via fd on dir type
    g = subprocess.run(["fd", "^\\.git$", ROOT, "--type", "d", "--hidden", "--max-depth", "4"],
                       capture_output=True, text=True)
    repos = sorted(os.path.relpath(x, ROOT) for x in g.stdout.split() if x)

    summary = {
        "root": ROOT,
        "total_files": int(len(df)),
        "total_bytes": int(df["bytes"].sum()),
        "top_dirs": by_top.head(25).to_dict("records"),
        "recent_7d_files": int(len(recent)),
        "git_repos": repos,
        "elapsed_s": round(time.time() - t0, 1),
    }
    json.dump(summary, open(f"{OUT}/summary.json", "w"), indent=1)
    print(json.dumps({k: v for k, v in summary.items() if k != "top_dirs"}, indent=1))
    print(f"wrote {OUT}/inventory.parquet ({len(df)} rows)")


if __name__ == "__main__":
    main()
