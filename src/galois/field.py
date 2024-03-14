import numpy as np
from .type import *
from src.cstyle import *


class Field:
  """Galois Field
  """
  def __init__(self, m: int, prim: VecLike) -> None:
    """Create GF(2^m).

    Args:
        m (int): m in GF(2^m)
        prim (VecLike): primitive polynomial
    """
    self.m = m
    self.prim = prim
    self._e2v: dict[ExpLike, VecLike] = {}
    self._v2e: dict[VecLike, ExpLike] = {}
    self._build()
  
  def _build(self):
    self._e2v[0] = 1

    for i in range(1, 1 << self.m):
      self._e2v[i] = self._e2v[i - 1] << 1
      if self._e2v[i] >> self.m & 1:
        self._e2v[i] ^= self.prim
      self._v2e[self._e2v[i]] = i
    
    self._v2e[0] = -1
    self._v2e[1] = 0
    
  def e2v(self, e: ExpLike) -> VecLike:
    """(strict) Convert exponent to vector.
    """
    return self._e2v[e]
  
  def v2e(self, v: VecLike) -> ExpLike:
    """(strict) Convert vector to exponent.
    """
    return self._v2e[v]
  
  def v2p(self, v: VecLike) -> PolyLike:
    """(strict) Convert vector to polynomial.
    """
    return np.array([int(x) for x in bin(v)[2:].zfill(self.m)], dtype=int)
  
  def p2v(self, p: PolyLike) -> VecLike:
    """(strict) Convert polynomial to vector.
    """
    return sum(p[i] << (len(p) - 1 - i) for i in range(len(p)))

  def p2e(self, p: PolyLike) -> ExpLike:
    """(strict) Convert polynomial to exponent.
    """
    return self.v2e(self.p2v(p))
  
  def e2p(self, e: ExpLike) -> PolyLike:
    """(strict) Convert exponent to polynomial.
    """
    return self.v2p(self.e2v(e))

  def normalize_e(self, e: int) -> int:
    """Normalize exponent to the range [0, 2^m - 2].
    """
    return e % ((1 << self.m) - 1)
  
  def add(self, p1: PolyLike, p2: PolyLike) -> PolyLike:
    """(strict) Add two polynomials.
    """
    v1 = self.p2v(p1)
    v2 = self.p2v(p2)
    return self.v2p(v1 ^ v2)

  def mul(self, p1: PolyLike, p2: PolyLike) -> PolyLike:
    """(strict) Multiply two polynomials.
    """
    e1 = self.p2e(p1)
    e2 = self.p2e(p2)
    return self.e2p(self.normalize_e(e1 + e2))
  
  def inv(self, p: PolyLike) -> PolyLike:
    """(strict) Get p_ret which satisfies p * p_ret = 1.
    """
    return p if np.all(p == 0) else self.e2p(((1 << self.m) - 1) - self.p2e(p))

  def cstyle(self) -> str:
    var_str = \
f"""
int m = {self.m};

{cstyle_vec(np.array(list(self._e2v.values())), 'e2v')}
{cstyle_vec(np.array(list(self._v2e.values())), 'v2e')}
"""
    fun_str = \
"""
int gf_normalize_e(int e)
{
  return e % ((1 << m) - 1);
}

int gf_add(int lhs, int rhs)
{
  return lhs ^ rhs;
}

int gf_mul(int lhs, int rhs)
{
  int elhs = v2e[lhs];
  int erhs = v2e[rhs];
  int emul = gf_normalize_e(elhs + erhs);

  return e2v[emul];
}

int gf_inv(int vec)
{
  int exp = v2e[vec];
  int inv_exp = exp ? ((1 << m) - 1) - exp : 0;
  int inv_vec = e2p[inv_exp];

  return inv_vec;
}
"""
    return var_str + fun_str
