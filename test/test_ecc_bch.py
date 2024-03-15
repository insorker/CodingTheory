import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.ecc.bch import *
from test_auto import *


def test_hamming_code():
  n, k, d, t, g = 15, 11, 3, 1, 0b10011
  m, prim = 4, 0b10011
  ecc = BCH(n, k, d, t, Field(m, prim), g)

  test_auto_overall(n, k, t, ecc)


test_hamming_code()