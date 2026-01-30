from __future__ import annotations

import csv
from pathlib import Path


def save_csv(outpath: str | Path, E_vals, R_vals, T_vals) -> Path:
    outpath = Path(outpath)
    outpath.parent.mkdir(parents=True, exist_ok=True)

    with outpath.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["E", "R", "T"])
        for E, R, T in zip(E_vals, R_vals, T_vals):
            w.writerow([float(E), float(R), float(T)])

    return outpath
