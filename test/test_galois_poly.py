import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import src.galois.poly as poly
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

assert (np.trim_zeros(r1, 'f') == poly.mod(x1, g)).all()
assert (np.trim_zeros(r2, 'f') == poly.mod(x2, g)).all()
assert (np.trim_zeros(r3, 'f') == poly.mod(x3, g)).all()
assert (np.trim_zeros(r4, 'f') == poly.mod(x4, g)).all()