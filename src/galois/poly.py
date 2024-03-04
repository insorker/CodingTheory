import numpy as np


def poly_add(lhs: np.ndarray, rhs: np.ndarray) -> np.ndarray:
  return lhs ^ rhs


def poly_mod(lhs: np.ndarray, rhs: np.ndarray) -> np.ndarray:
  minuend = np.trim_zeros(lhs, 'f')
  subtrahend_base = np.trim_zeros(rhs, 'f')

  while len(minuend) >= len(rhs):
    subtrahend = np.pad(subtrahend_base, (0, len(minuend) - len(subtrahend_base)))
    minuend = poly_add(minuend, subtrahend)
    minuend = np.trim_zeros(minuend, 'f')
  
  return minuend
