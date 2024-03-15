import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.ecc.hamming import *
from tools import *


for m in range(2, 5):
  ecc = Hamming(m)
  test_auto_overall(ecc.n, ecc.k, 1, ecc)