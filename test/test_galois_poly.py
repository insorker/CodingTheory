import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.galois.poly import *
import numpy as np


g = np.array([1, 1, 0, 1])
x1 = np.array([1, 0, 0, 0, 0, 0, 0])
x2 = np.array([0, 1, 0, 0, 0, 0, 0])
x3 = np.array([0, 0, 1, 0, 0, 0, 0])
x4 = np.array([0, 0, 0, 1, 0, 0, 0])
r1 = np.array([0, 1, 1, 0])
r2 = np.array([0, 0, 1, 1])
r3 = np.array([0, 1, 1, 1])
r4 = np.array([0, 1, 0, 1])

assert (np.trim_zeros(r1, 'f') == poly_mod(x1, g)).all()
assert (np.trim_zeros(r2, 'f') == poly_mod(x2, g)).all()
assert (np.trim_zeros(r3, 'f') == poly_mod(x3, g)).all()
assert (np.trim_zeros(r4, 'f') == poly_mod(x4, g)).all()