from __future__ import annotations

import numpy as np 
from typing import Callable, Union

ArrayLike = Union[float, np.ndarray]

def TanhPotential(a: float, b: float):
    """Creates a tanh potential function.

    Args:
        a (float): Amplitude of the potential.
        b (float): Steepness of the potential.

    Returns:
        Callable[[ArrayLike], ArrayLike]: A function that computes the tanh potential.
    """
    def V(x: ArrayLike) -> ArrayLike:
        xarr = np.asarray(x)
        return a * np.tanh(b * xarr)
    V_L, V_R = -float(a), float(a)
    label = rf"$V(x) = {a} \tanh({b} x)$"
    return V, V_L, V_R, label

def expTanhPotential(a: float, b: float, c: float):
    """Creates an exponential tanh potential function.

    Args:
        a (float): Amplitude of the potential.
        b (float): Steepness of the potential.
        c (float): Exponential decay rate.

    Returns:
        Callable[[ArrayLike], ArrayLike]: A function that computes the exponential tanh potential.
    """
    def V(x: ArrayLike) -> ArrayLike:
        xarr = np.asarray(x)
        return a * np.exp(b* np.tanh(c * xarr))

    V_L, V_R = float(a * np.exp(-b)), float(a * np.exp(b))
    label = rf"$V(x) = {a} e^{{{b} \tanh({c} x)}}$" 
    return V, V_L, V_R, label

def woodsSaxonPotential(V0: float, a: float, b: float):
    """Creates a Woods-Saxon potential function.

    Args:
        V0 (float): Depth of the potential well.
        a (float): Steepness of the potential.
        b (float): Width parameter of the potential."""
    # Implement the double Woods-Saxon step shown in the image:
    # V(x) = V0 * [ Θ(-x)/(1 + exp(-a*(x + L)))  +  Θ(x)/(1 + exp(a*(x - L))) ]
    # where b plays the role of L (half-width of the plateau) and a is the
    # diffuseness. This yields V ~ V0 for -L < x < L and V -> 0 for |x| -> inf.
    L = b
    def V(x: ArrayLike) -> ArrayLike:
        xarr = np.asarray(x)
        # create output with same shape
        out = np.zeros_like(xarr, dtype=float)
        # left piece (Θ(-x)): active for x < 0
        mask_left = xarr < 0
        if np.any(mask_left):
            xl = xarr[mask_left]
            out[mask_left] = 1.0 / (1.0 + np.exp(-a * (xl + L)))
        # right piece (Θ(x)): active for x >= 0
        mask_right = xarr >= 0
        if np.any(mask_right):
            xr = xarr[mask_right]
            out[mask_right] = out[mask_right] + 1.0 / (1.0 + np.exp(a * (xr - L)))
        return float(V0) * out

    V_L = 0.0
    V_R = 0.0
    label = rf"$V(x) = {V0}\left[ \frac{{\Theta(-x)}}{{1+e^{{- {a}(x+{L})}}}} + \frac{{\Theta(x)}}{{1+e^{{{a}(x-{L})}}}} \right]$"
    return V, V_L, V_R, label
            