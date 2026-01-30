from __future__ import annotations

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


def plot_potential(model, num_points: int = 600, outpath: str | Path | None = None, show: bool = False):
    x = np.linspace(model.XMIN, model.XMAX, num_points)
    Vx = model.V_of_x(x)

    plt.figure(figsize=(7, 4))
    plt.plot(x, Vx)
    plt.title(model.potential_label)
    plt.xlabel("x")
    plt.ylabel("V(x)")
    plt.grid(True, alpha=0.3)

    if outpath is not None:
        outpath = Path(outpath)
        outpath.parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(outpath, dpi=160, bbox_inches="tight")

    if show:
        plt.show()
    plt.close()


def plot_RT(E, R, T, outpath: str | Path | None = None, show: bool = False, title: str = "Scattering"):
    plt.figure(figsize=(7, 4))
    plt.plot(E, R, label="R")
    plt.plot(E, T, label="T")
    plt.xlabel("E")
    plt.ylabel("Coefficient")
    plt.title(title)
    plt.grid(True, alpha=0.3)
    plt.legend()

    if outpath is not None:
        outpath = Path(outpath)
        outpath.parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(outpath, dpi=160, bbox_inches="tight")

    if show:
        plt.show()
    plt.close()
