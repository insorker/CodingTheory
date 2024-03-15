import numpy as np
from functools import reduce
from .base import EccBase
import src.galois.poly as poly
from src.galois.type import *


class Hamming(EccBase):
  def __init__(self, m: int):
    self.n = (1 << m) - 1
    self.k = (1 << m) - m - 1
    self.check_idx = [1]
    self._build()
  
  def _build(self):
    while len(self.check_idx) + self.k >= (1 << len(self.check_idx)):
      self.check_idx.append(self.check_idx[-1] << 1)
  
  def encode(self, msg: PolyLike) -> PolyLike:
    codeword = poly.create(0, len(self.check_idx) + len(msg))

    data_idx = 0
    for i in self.check_idx:
      data_length = i - 1
      codeword[i: i + data_length] = msg[data_idx: data_idx + data_length]
      data_idx += data_length
    
    for i in self.check_idx:
      codeword[i - 1] = reduce(lambda x, y: x ^ y, [bit for (j, ), bit in np.ndenumerate(codeword) if (j + 1) % (2 * i) >= i])
    
    return codeword

  def decode(self, msg: PolyLike) -> PolyLike:
    msg = msg.copy()
    err = self.error_position(msg)
    if err != 0:
      msg[err - 1] = 1 - msg[err - 1]

    result = poly.create(0, self.k)

    data_idx = 0
    for i in self.check_idx:
      data_length = i - 1
      result[data_idx: data_idx + data_length] = msg[i: i + data_length]
      data_idx += data_length
    return result

  def error_position(self, msg: PolyLike) -> int:
    return reduce(lambda x, y: x ^ y, [i + 1 for (i, ), bit in np.ndenumerate(msg) if bit], 0)