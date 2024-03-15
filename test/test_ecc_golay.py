import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.ecc.golay import *
from tools import *


def test_24_12():
  n, k, t = 24, 12, 3
  ecc = Golay_24_12_8()
  test_auto_rand(n, k, t, ecc)


test_24_12()