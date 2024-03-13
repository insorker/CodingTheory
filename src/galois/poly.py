import numpy as np
from .type import *


def poly_norm(poly: PolyLike) -> PolyLike:
  return poly % 2


def vec2poly(vec: VecLike, len: int) -> PolyLike:
  return np.array([int(x) for x in bin(vec)[2:].zfill(len)], dtype=int)


def poly2vec(poly: PolyLike) -> VecLike:
  return sum(poly[i] << (len(poly) - 1 - i) for i in range(len(poly)))


def poly_add(lhs: PolyLike, rhs: PolyLike) -> PolyLike:
  return lhs ^ rhs


def poly_mod(lhs: PolyLike, rhs: PolyLike) -> PolyLike:
  minuend = np.trim_zeros(lhs, 'f')
  subtrahend_base = np.trim_zeros(rhs, 'f')

  while len(minuend) >= len(rhs):
    subtrahend = np.pad(subtrahend_base, (0, len(minuend) - len(subtrahend_base)))
    minuend = poly_add(minuend, subtrahend)
    minuend = np.trim_zeros(minuend, 'f')
  
  return minuend


def poly_shift(poly: PolyLike, shift: int) -> PolyLike:
  shift = (shift + len(poly)) % len(poly)
  return np.concatenate((poly[shift:], poly[:shift]))


def poly_wt(word: PolyLike) -> int:
  cnt = 0
  for i in word:
    cnt += i == 1
  return cnt


def poly_dist(lhs: PolyLike, rhs: PolyLike):
  return poly_wt(poly_add(lhs, rhs))