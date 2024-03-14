import numpy as np
from .type import *


def create(vec: VecLike, len: int = 0) -> PolyLike:
  """Create a polynomial from vector. If length of result is less than `len`, pad result with zeros on the left.
  """
  return np.array([int(x) for x in bin(vec)[2:].zfill(len)], dtype=int)


def normalize(poly: PolyLike) -> PolyLike:
  """Normalize elements of polynomial to 1 or 0.
  """
  return (poly % 2).astype(int)


def wt(word: PolyLike) -> int:
  """Get the hamming weight of word.
  """
  return np.sum(word == 1)


def dist(lhs: PolyLike, rhs: PolyLike):
  """Get the hamming distance of word.
  """
  return wt(add(lhs, rhs))


def add(lhs: PolyLike, rhs: PolyLike) -> PolyLike:
  """Add two polynomials.
  """
  return lhs ^ rhs


def mod(lhs: PolyLike, rhs: PolyLike) -> PolyLike:
  """lhs modulo rhs.
  """
  minuend = np.trim_zeros(lhs, 'f')
  subtrahend_base = np.trim_zeros(rhs, 'f')

  while len(minuend) >= len(rhs):
    subtrahend = np.pad(subtrahend_base, (0, len(minuend) - len(subtrahend_base)))
    minuend = add(minuend, subtrahend)
    minuend = np.trim_zeros(minuend, 'f')
  
  return minuend


def shift(poly: PolyLike, shift: int) -> PolyLike:
  """`shift` > 0: left shift; `shift` < 0: right shift; `shift` = 0: no shift.
  """
  shift = (shift + len(poly)) % len(poly)
  return np.concatenate((poly[shift:], poly[:shift]))