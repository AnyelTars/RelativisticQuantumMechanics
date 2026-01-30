from __future__ import annotations

import numpy as np


def conservation_metrics(E_vals, R_vals, T_vals, tol_R_gt_1: float = 1.01, tol_T_lt_0: float = -0.01):
    RT = R_vals + T_vals
    metrics = {
        "avg_R_plus_T": float(np.nanmean(RT)),
        "std_R_plus_T": float(np.nanstd(RT)),
        "max_abs_R_plus_T_minus_1": float(np.nanmax(np.abs(RT - 1.0))),
        "count_R_gt_1": int(np.sum(R_vals > tol_R_gt_1)),
        "max_R": float(np.nanmax(R_vals)),
        "count_T_lt_0": int(np.sum(T_vals < tol_T_lt_0)),
        "min_T": float(np.nanmin(T_vals)),
        "N": int(len(E_vals)),
        "E_min": float(np.nanmin(E_vals)),
        "E_max": float(np.nanmax(E_vals)),
    }
    return metrics
