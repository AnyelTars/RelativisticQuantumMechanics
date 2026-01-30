from __future__ import annotations

import numpy as np 
from dataclasses import dataclass
from typing import Callable, Union

ArrayLike = Union[float, np.ndarray]

@dataclass
class RiccatiModel:
    #physics
    m: float
    V: Callable[[ArrayLike], ArrayLike]
    V_L: float
    V_R: float
    potential_label: str = r"$V(x)$"

    # Numerics
    XMIN: float = -10.0
    XMAX: float = 10.0
    N_STEPS: int = 6000
    Y_MAX: float = 1e6
    EPS_DENOM: float = 1e-12

    def V_of_x(self, x: ArrayLike) -> ArrayLike:
        return self.V(x)
    
    @property
    def VL(self) -> float:
        return float(self.V_L)
    
    @property
    def VR(self) -> float:
        return float(self.V_R)  
    
    @property
    def E_sr(self) -> float:
        return self.VR - self.m
    
    @property
    def E_sl(self) -> float:
        return self.VL - self.m
    
    @property
    def E_prop(self) -> float:
        return self.VR +self.m
    
    @property
    def E_pml(self) -> float:
        return self.VL + self.m
    
    def local_k(self,E: float, x: float) -> complex:
        """Local momentum function k(x)"""
        Vx = self.V_of_x(x)
        z = (E - Vx)**2 - self.m**2
        return np.sqrt(z + 0j)  # Ensure complex output for negative values 
    
    def asymtotic_k(self, E: float, V_asym: float) -> complex:
        """Asymptotic momentum function k_asymptotic"""
        z = (E - V_asym)**2 - self.m**2
        k = np.sqrt(z + 0j)  # Ensure complex output for negative values
        # Fix sig for real k to keep consistent propagation direction
        if abs(k.imag) < 1e-14:
            base = abs(k.real)
            sgn = 1.0 if (E - V_asym) >= 0 else -1.0
            return sgn * base + 0j
        return k

    def riccati_rhs(self, x: float, y: complex, E: float) -> complex:
        """Right-hand side of the Riccati equation dy/dx = f(x,y)"""
        k = self.local_k(E, x)
        return -y * y - k*k

    def integrate_riccati(self, E: float) -> complex:
        """Integrate the Riccati equation from XMIN to XMAX for a given energy E using the RK4 method."""
        # Integrate from the right asymptotic region (XMAX) back to the left
        # (XMIN). This keeps the initial condition at the right propagating
        # wave (y = i kR) and integrates towards the matching point on the left.
        xR = self.XMAX
        xL = self.XMIN
        h = (xL - xR) / self.N_STEPS  # negative step
        kR = self.asymtotic_k(E, self.V_R)
        y = 1j * kR  # Initial condition at x = XMAX (right asymptote)
        x = xR

        for _ in range(self.N_STEPS):
            k1 = self.riccati_rhs(x,           y,             E)
            k2 = self.riccati_rhs(x + 0.5*h,   y + 0.5*h*k1,  E)
            k3 = self.riccati_rhs(x + 0.5*h,   y + 0.5*h*k2,  E)
            k4 = self.riccati_rhs(x + h,       y + h*k3,      E)
            y += (h/6.0)*(k1 + 2*k2 + 2*k3 + k4)
            x += h
            mag = abs(y)
            if mag > self.Y_MAX:
                y = y * (self.Y_MAX / mag)
        return y

    def scattering_coeffs(self, E:float) -> tuple[float, float]:
        """Calculate reflection and transmission coefficients for a given energy E."""
        # Left asymptotic check: need propagating mode on the left to have
        # a well-defined incoming wave from the left.
        zL = (E - self.VL)**2 - self.m**2
        if zL <= 0:
            return 0.0, 0.0

        yL = self.integrate_riccati(E)
        kL = self.asymtotic_k(E, self.VL)
        xL = self.XMIN

        phase_factor = np.exp(2j * kL * xL)
        # Sign convention restored to match the previously working form
        denom = yL + 1j * kL
        if abs(denom) < self.EPS_DENOM:
            denom = denom + self.EPS_DENOM

        R_amp = phase_factor * (1j * kL - yL) / denom
        R_prob = float(np.abs(R_amp)**2)

        # Right asymptotic evanescent check: if right is evanescent, total
        # reflection is expected (T ~ 0).
        zR = (E - self.VR)**2 - self.m**2
        if zR <= 0:
            return 1.0, 0.0

        T_prob = float(1.0 - R_prob)
        return R_prob, T_prob

    def compute_RT_spectrum(self, E_min: float = 0.0, E_max: float = 15.0, nE: int = 1000):
        """Compute reflection and transmission coefficients over an energy range."""
        E_vals  = np.linspace(E_min, E_max, int(nE))
        R_vals  = np.empty_like(E_vals, dtype=float)
        T_vals  = np.empty_like(E_vals, dtype=float)

        for i, E in enumerate(E_vals):
            R_vals[i], T_vals[i] = self.scattering_coeffs(float(E))

        return E_vals, R_vals, T_vals
        