import numpy as np


def poly_add(lhs: np.ndarray, rhs: np.ndarray) -> np.ndarray:
  return lhs ^ rhs


def poly_mod(lhs: np.ndarray, rhs: np.ndarray) -> np.ndarray:
  minuend = lhs

  while len(minuend) >= len(rhs):
    subtrahend = np.pad(rhs, (0, len(minuend) - len(rhs)))
    minuend = poly_add(minuend, subtrahend)
  
  return minuend
