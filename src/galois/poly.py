import numpy as np
from .type import *


def poly_norm(poly: PolyLike) -> PolyLike:
  """normalize elements of polynomial to 1 or 0

  Args:
      poly (PolyLike): polynomial

  Returns:
      PolyLike: polynomial
  """
  return poly % 2


def vec2poly(vec: VecLike, len: int) -> PolyLike:
  """convert vector to polynomial

  Args:
      vec (VecLike): vector
      len (int): length of polynomial

  Returns:
      PolyLike: polynomial
  """
  return np.array([int(x) for x in bin(vec)[2:].zfill(len)], dtype=int)


def poly2vec(poly: PolyLike) -> VecLike:
  """convert polynomial to vector

  Args:
      poly (PolyLike): polynomial

  Returns:
      VecLike: vector
  """
  return sum(poly[i] << (len(poly) - 1 - i) for i in range(len(poly)))


def poly_add(lhs: PolyLike, rhs: PolyLike) -> PolyLike:
  """add two polynomial

  Args:
      lhs (PolyLike): _description_
      rhs (PolyLike): _description_

  Returns:
      PolyLike: _description_
  """
  return lhs ^ rhs


def poly_mod(lhs: PolyLike, rhs: PolyLike) -> PolyLike:
  """get lhs mod rhs

  Args:
      lhs (PolyLike): _description_
      rhs (PolyLike): _description_

  Returns:
      PolyLike: _description_
  """
  minuend = np.trim_zeros(lhs, 'f')
  subtrahend_base = np.trim_zeros(rhs, 'f')

  while len(minuend) >= len(rhs):
    subtrahend = np.pad(subtrahend_base, (0, len(minuend) - len(subtrahend_base)))
    minuend = poly_add(minuend, subtrahend)
    minuend = np.trim_zeros(minuend, 'f')
  
  return minuend


def poly_shift(poly: PolyLike, shift: int) -> PolyLike:
  """shift > 0: left shift ; shift < 0: right shift ; shift = 0: no shift

  Args:
      poly (PolyLike): _description_
      shift (int): [-len(poly), len(poly)]

  Returns:
      PolyLike: _description_
  """
  shift = (shift + len(poly)) % len(poly)
  return np.concatenate((poly[shift:], poly[:shift]))


def poly_wt(word: PolyLike) -> int:
  """hamming weight

  Args:
      word (PolyLike): _description_

  Returns:
      int: _description_
  """
  cnt = 0
  for i in word:
    cnt += i == 1
  return cnt


def poly_dist(lhs: PolyLike, rhs: PolyLike):
  """hamming distance

  Args:
      lhs (PolyLike): _description_
      rhs (PolyLike): _description_

  Returns:
      _type_: _description_
  """
  return poly_wt(poly_add(lhs, rhs))