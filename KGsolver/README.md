# KGsolver

`KGsolver` is a small Python package for studying one-dimensional scattering in the Klein-Gordon equation with a Riccati-equation approach. It is intended for numerical experiments with smooth potential profiles and for generating the reflection and transmission curves used in the accompanying research work.

The repository contains:

- A Python package in `src/KGsolver/`
- An example notebook in `notebooks/examples.ipynb`
- Figure/data folders in `notebooks/` used for the paper
- Analytic comparison data for the tanh potential in `Analytic-data/`

## What this repository does

The code builds a potential \(V(x)\), defines the corresponding Klein-Gordon scattering model, integrates the Riccati equation numerically, and computes:

- Reflection coefficient `R(E)`
- Transmission coefficient `T(E)`
- Basic conservation diagnostics such as `R + T`

The currently implemented potentials are:

- Hyperbolic tangent potential
- Exponential tanh potential
- Woods-Saxon-type potential
- "Cups" exponential potential

## Repository structure

```text
KGsolver/
├── Analytic-data/         # Analytic tanh reference data
├── notebooks/             # Example notebook and paper figures
├── results/               # Typical CLI outputs
├── src/KGsolver/          # Installable Python package
├── pyproject.toml         # Package metadata
└── README.md
```

The main source files are:

- `src/KGsolver/potentials.py`: potential factories
- `src/KGsolver/riccati.py`: `RiccatiModel` and the numerical solver
- `src/KGsolver/spectrum.py`: conservation metrics
- `src/KGsolver/plotting.py`: helper plotting functions
- `src/KGsolver/io.py`: CSV export helpers
- `src/KGsolver/cli.py`: command-line interface

## Installation

### Requirements

- Python 3.10 or newer
- `numpy`
- `matplotlib`

These are already declared in `pyproject.toml`.

Optional for running the notebook:

- `pandas`
- Jupyter Notebook or JupyterLab

### Standard installation

From the repository root:

```bash
python -m pip install .
```

### Editable installation for development

```bash
python -m pip install -e .
```

After installation, the command-line entry point `kgsolver` should be available.

## How to use the package

### 1. Import the package in Python

```python
import KGsolver as kg
from KGsolver import RiccatiModel
```

### 2. Choose a potential

Each potential factory returns four objects:

```python
V, VL, VR, label = ...
```

where:

- `V` is the callable potential function
- `VL` is the left asymptotic value
- `VR` is the right asymptotic value
- `label` is a LaTeX-style label for plots

Example with the tanh potential:

```python
V, VL, VR, label = kg.TanhPotential(a=5, b=1)
```

### 3. Build the scattering model

```python
model = RiccatiModel(
    m=1,
    V=V,
    V_L=VL,
    V_R=VR,
    potential_label=label,
    XMIN=-10,
    XMAX=10,
    N_STEPS=6000,
)
```

Important parameters:

- `m`: particle mass
- `XMIN`, `XMAX`: numerical integration interval
- `N_STEPS`: number of RK4 steps used in the Riccati integration

### 4. Compute scattering at a single energy

```python
R, T = model.scattering_coeffs(3.0)
print(R, T, R + T)
```

### 5. Compute a full spectrum

```python
E, R, T = model.compute_RT_spectrum(E_min=0.1, E_max=10, nE=200)
```

### 6. Save or analyze the results

```python
from KGsolver.io import save_csv
from KGsolver.spectrum import conservation_metrics

save_csv("results/RT.csv", E, R, T)
metrics = conservation_metrics(E, R, T)
print(metrics)
```

### 7. Plot the potential and the coefficients

```python
from KGsolver.plotting import plot_potential, plot_RT

plot_potential(model, outpath="results/potential.png")
plot_RT(E, R, T, outpath="results/RT.png", title="tanh potential")
```

## Example script

This minimal example reproduces the standard workflow:

```python
import KGsolver as kg
from KGsolver import RiccatiModel
from KGsolver.io import save_csv
from KGsolver.plotting import plot_potential, plot_RT

V, VL, VR, label = kg.expTanhPotential(a=-5, b=1, c=1)

model = RiccatiModel(
    m=1,
    V=V,
    V_L=VL,
    V_R=VR,
    potential_label=label,
    XMIN=-10,
    XMAX=10,
    N_STEPS=8000,
)

E, R, T = model.compute_RT_spectrum(E_min=-10, E_max=1, nE=600)

save_csv("results/exptanh.csv", E, R, T)
plot_potential(model, outpath="results/exptanh_potential.png")
plot_RT(E, R, T, outpath="results/exptanh_RT.png", title="exp-tanh")
```

## Command-line usage

The package also provides a CLI.

### Single-energy calculation

```bash
kgsolver run --potential tanh --m 1 --E 3.0 --V0 5 --a 5 --b 1
```

### Energy sweep with CSV and plots

```bash
kgsolver sweep \
  --potential exp-tanh \
  --m 1 \
  --V0 5 \
  --a -5 \
  --b 1 \
  --c 1 \
  --Emin -10 \
  --Emax 1 \
  --nE 600 \
  --out results \
  --plot
```

This writes:

- `results/RT.csv`
- `results/potential.png`
- `results/RT.png`

To see all CLI options:

```bash
kgsolver --help
```

## Example notebook

The main example notebook is:

- `notebooks/examples.ipynb`

This notebook shows how the package was used to:

- define potentials
- compute `R(E)` and `T(E)`
- save CSV data
- produce the figures used in the paper
- compare the tanh numerical results with analytic reference data

If you want to understand the practical workflow of the package, this notebook is the best starting point.

There is also an additional notebook:

- `notebooks/Billiard.ipynb`

This notebook is kept with the other notebook material, but it is separate from the `KGsolver` package itself.

## Notes on the current numerical model

This repository is intended for research and exploration, so it is important to be explicit about its current behavior:

- The code enforces and reports conservation checks through `R + T`
- For some energies and parameter choices, the numerical method can produce `R > 1` and `T < 0` while still preserving `R + T = 1`
- The notebook includes some figure-specific post-processing and plotting choices used for the paper
- The tanh comparisons rely on reference files stored in `Analytic-data/`

These points do not make the repository unusable, but they should be kept in mind when interpreting results.

## Recommended workflow for a new user

1. Install the package with `python -m pip install -e .`
2. Open `notebooks/examples.ipynb`
3. Run the notebook cells to reproduce the examples
4. Use the Python API or `kgsolver` CLI for your own potentials and parameter sweeps

## Author

Angel Salazar
