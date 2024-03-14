import numpy as np
import src.galois.poly as poly
from src.galois.field import *
from src.cstyle import *


class BCH:
  def __init__(self, n: int, k: int, d: int, t: int, gf: Field, g: VecLike):
    self.n = n
    self.k = k
    self.d = d
    self.t = t
    self.gf = gf
    self.g = gf.v2p(g)
  
  def get_g_matrix(self) -> np.ndarray:
    g = np.zeros((self.k, self.n), dtype=int)

    for i in range(0, self.k):
      g[i][i] = 1
      # r_i = x^(n - i) mod g, i = 1,2,...,k
      r = poly.mod(self.gf.v2p(1 << (self.n - i - 1)), self.g)
      # 使 r 与 g[i] 对齐
      r = np.pad(r, (self.n - len(r), 0))
      g[i] = poly.add(g[i], r)

    return g
    
  def get_h_matrix(self) -> np.ndarray:
    h = np.zeros((self.t * self.gf.m, self.n), dtype=int)

    for i in range(0, self.t):
      for j in range(0, self.n):
        e = self.gf.norm_e((2 * i + 1) * (self.n - 1 - j))
        p = self.gf.e2p(e)

        for k in range(0, self.gf.m):
          h[i * self.gf.m + k][j] = p[k]
    
    return h

  def get_s(self, codeword: np.ndarray) -> np.ndarray:
    h = self.get_h_matrix()
    s = (codeword @ h.T) % 2
    return np.array(np.split(s, self.t))

  def encode(self, msg: np.ndarray) -> np.ndarray:
    return (msg @ self.get_g_matrix()) % 2
  
  def decode_t1(self, codeword: np.ndarray) -> np.ndarray:
    s = self.get_s(codeword)[0]
    s_inv = self.gf.inv(s)
    err_pos = self.gf.p2e(s_inv)

    if err_pos != -1:
      codeword[err_pos - 1] = 1 - codeword[err_pos - 1]

    return codeword[0: self.k]

  def cstyle(self):
    g = self.get_g_matrix()
    h = self.get_h_matrix().T
    var_str = \
f"""
{cstyle_mt(g, 'g')}
{cstyle_mt(h, 'h')}
int s[{self.gf.m}] = {{ }};
"""
    fun_str = \
f"""
"""
# void get_syndrome(int *codeword)
# {{
#   {';'.join(map(str, [f's[{i}] = {"^".join(map(str, [f"(codeword[{j}] * h[{j}][{i}])" for j in range(0, self.n)]))}' for i in range(0, self.gf.m)]))};
# }}
# """
    return var_str + fun_str