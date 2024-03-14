import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.ecc import bch
from src.galois import field
from src.galois.type import *
import random
import numpy as np


def sim_err(codeword: PolyLike, n: int) -> PolyLike:
  err_pos = random.randint(0, n - 1)
  codeword_err = codeword
  codeword_err[err_pos] = 1 - codeword_err[err_pos]
  return codeword_err


def test():
  b = bch.BCH(15, 11, 3, 1, field.Field(4, 0b10011), 0b10011)

  for _ in range(0, 10):
    msg_send = np.random.randint(0, 2, size=b.k)
    codeword_send = b.encode(msg_send)
    codeword_recv = sim_err(codeword_send, b.n)
    msg_recv = b.decode_t1(codeword_recv)
    if not np.array_equal(msg_send, msg_recv):
      print("error")


test()
