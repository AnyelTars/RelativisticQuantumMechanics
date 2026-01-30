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