import numpy as np
from src.galois.field import *
from src.galois.poly import *
from src.galois.type import *
from src.cstyle import *


class Golay_24_12:
  def __init__(self):
    self.g = vec2poly(0b11011100010, 11)
    self.B = np.array(vec2poly(0b111111111110, 12), dtype=int)
    for i in range(1, 12):
      self.B = np.vstack((np.append(poly_shift(self.g, -i), 1), self.B))
    self.G = np.concatenate((np.eye(12, dtype=int), self.B), axis=1)
    self.H_1 = np.concatenate((np.eye(12, dtype=int), self.B))
    self.H_2 = np.concatenate((self.B, np.eye(12, dtype=int)))

  def encode(self, msg: PolyLike) -> PolyLike:
    return poly_norm(msg @ self.G)

  def decode(self, msg: PolyLike) -> PolyLike:
    s1 = poly_norm(msg @ self.H_1)

    if poly_wt(s1) <= 3:
      u = np.concatenate((s1, np.zeros(12, dtype=int)))
      return poly_add(msg, u)
    else:
      for i in range(0, 12):
        if poly_wt(poly_add(s1, self.B[i])) <= 2:
          u = np.concatenate((poly_add(s1, self.B[i]), np.pad([1], (i, 11 - i))))
          return poly_add(msg, u)
    
    s2 = poly_norm(msg @ self.H_2)
    if poly_wt(s2) <= 3:
      u = np.concatenate((s2, np.eye(12, dtype=int)))
      return poly_add(msg, u)
    else:
      for i in range(0, 12):
        if poly_wt(poly_add(s2, self.B[i])) <= 2:
          u = np.concatenate((np.pad([1], (i, 11 - i)), poly_add(s2, self.B[i])))
          return poly_add(msg, u)
        
    return np.array([])