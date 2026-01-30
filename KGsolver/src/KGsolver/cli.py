from __future__ import annotations

import argparse
from operator import sub
from pathlib import Path

from .riccati import RiccatiModel
from .potentials import TanhPotential, expTanhPotential, woodsSaxonPotential
from .io import save_csv
from .plotting import plot_RT, plot_potential
from .spectrum import conservation_metrics


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="kgsolver", description="KG 1D scattering (Riccati)")

    sub = p.add_subparsers(dest="cmd", required=True)

        # Common potential args are handled per command for simplicity
    POTENTIAL_CHOICES = ["woods-saxon", "tanh", "exp-tanh"]

    run = sub.add_parser("run", help="Compute R,T for a single energy E")
    run.add_argument("--potential", choices=POTENTIAL_CHOICES, required=True)
    run.add_argument("--m", type=float, required=True)
    run.add_argument("--E", type=float, required=True)
    run.add_argument("--V0", type=float, required=True)
    run.add_argument("--a", type=float, required=True)
    run.add_argument("--b", type=float, default=1.0, help="Second shape parameter (for tanh/exp-tanh)")
    run.add_argument("--c", type=float, default=1.0, help="Third shape parameter (for exp-tanh)")
    run.add_argument("--x0", type=float, default=0.0)
    run.add_argument("--xmin", type=float, default=-10.0)
    run.add_argument("--xmax", type=float, default=10.0)
    run.add_argument("--nsteps", type=int, default=6000)

    sweep = sub.add_parser("sweep", help="Compute spectrum R(E), T(E)")
    sweep.add_argument("--potential", choices=POTENTIAL_CHOICES, required=True)
    sweep.add_argument("--m", type=float, required=True)
    sweep.add_argument("--V0", type=float, required=True)
    sweep.add_argument("--a", type=float, required=True)
    sweep.add_argument("--b", type=float, default=1.0)
    sweep.add_argument("--c", type=float, default=1.0)
    sweep.add_argument("--x0", type=float, default=0.0)
    sweep.add_argument("--Emin", type=float, required=True)
    sweep.add_argument("--Emax", type=float, required=True)
    sweep.add_argument("--nE", type=int, default=400)
    sweep.add_argument("--xmin", type=float, default=-10.0)
    sweep.add_argument("--xmax", type=float, default=10.0)
    sweep.add_argument("--nsteps", type=int, default=6000)
    sweep.add_argument("--out", type=str, default="results")
    sweep.add_argument("--plot", action="store_true")

    return p

def make_model(args) -> RiccatiModel:
    # 2. Lógica para seleccionar el potencial correcto
    #if args.potential == "square":
    #    V, VL, VR, label = square_barrier(V0=args.V0, a=args.a, x0=args.x0)
    if args.potential == "woods-saxon":
        V, VL, VR, label = woodsSaxonPotential(V0=args.V0, a=args.a, b=args.b)
    if args.potential == "tanh":
        # Usamos V0 como 'a' y args.a como 'b' para mantener consistencia con tus fórmulas
        V, VL, VR, label = TanhPotential(a=args.a, b=args.b)
    elif args.potential == "exp-tanh":
        V, VL, VR, label = expTanhPotential(a=args.a, b=args.b, c=args.c)

    model = RiccatiModel(
        m=args.m, V=V, V_L=VL, V_R=VR,
        potential_label=label,
        XMIN=args.xmin, XMAX=args.xmax, N_STEPS=args.nsteps,
    )
    return model

def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    model = make_model(args)

    if args.cmd == "run":
        R, T = model.scattering_coeffs(args.E)
        print(f"potential={args.potential}  m={args.m}  V0={args.V0}  a={args.a}  x0={args.x0}")
        print(f"E={args.E:.8g}")
        print(f"R={R:.10f}  T={T:.10f}  (R+T={R+T:.10f})")
        print(f"E_sr={model.E_sr:.8g}   E_prop={model.E_prop:.8g}")
        return

    if args.cmd == "sweep":
        E, R, T = model.compute_RT_spectrum(E_min=args.Emin, E_max=args.Emax, nE=args.nE)

        outdir = Path(args.out)
        csv_path = save_csv(outdir / "RT.csv", E, R, T)
        metrics = conservation_metrics(E, R, T)

        print(f"Saved: {csv_path}")
        print("Conservation metrics:")
        for k, v in metrics.items():
            print(f"  {k}: {v}")

        print(f"Theoretical window: E_sr={model.E_sr:.8g}, E_prop={model.E_prop:.8g}")

        if args.plot:
            plot_potential(model, outpath=outdir / "potential.png", show=False)
            plot_RT(E, R, T, outpath=outdir / "RT.png", show=False, title=f"{args.potential} (R,T)")
            print(f"Saved plots: {outdir/'potential.png'} , {outdir/'RT.png'}")


if __name__ == "__main__":
    main()
