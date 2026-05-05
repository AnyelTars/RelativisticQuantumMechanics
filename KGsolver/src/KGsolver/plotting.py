from __future__ import annotations

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["mathtext.fontset"] = "stix"
plt.rcParams["font.family"] = "STIXGeneral"


def _resolve_output_path(outpath: str | Path, default_name: str) -> Path:
    outpath = Path(outpath)
    if outpath.suffix:
        outpath.parent.mkdir(parents=True, exist_ok=True)
        return outpath

    outpath.mkdir(parents=True, exist_ok=True)
    return outpath / f"{default_name}.png"


def plot_potential(model, name_fig: str = "potential", num_points: int = 600, outpath: str | Path | None = None, show: bool = False):
    x = np.linspace(model.XMIN, model.XMAX, num_points)
    Vx = model.V_of_x(x)

    plt.figure(figsize=(8, 6))
    plt.plot(x, Vx, color="blue", linewidth=3, linestyle="-")
    #plt.title(model.potential_label)
    plt.xlabel(r"x", fontsize=22)
    plt.ylabel(r"V(x)", fontsize=22)
    plt.tick_params(axis='both', which='both', direction='in', labelsize=18, top=True, right=True, length=8, width=1.0)
    plt.tick_params(axis='x', pad=8)
    plt.xlim(model.XMIN, model.XMAX)
    plt.ylim(min(Vx) - 0.5, max(Vx) + 0.5)
    if outpath is not None:
        save_path = _resolve_output_path(outpath, name_fig)
        plt.savefig(save_path, dpi=300, bbox_inches="tight")

    if show:
        plt.show()
    plt.close()


def plot_RT(E, R, T, outpath: str | Path | None = None, show: bool = False, title: str = "Scattering"):
    plt.figure(figsize=(7, 4))
    plt.plot(E, R, label="R")
    plt.plot(E, T, label="T")
    plt.xlabel(r"E")
    plt.ylabel(r"Coefficient")
    plt.title(title)
    plt.grid(True, alpha=0.3)
    plt.legend()

    if outpath is not None:
        save_path = _resolve_output_path(outpath, title)
        plt.savefig(save_path, dpi=300, bbox_inches="tight")

    if show:
        plt.show()
    plt.close()
