import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.ecc.golay import *
from src.galois.poly import *


golay = Golay_24_12()


def test_1():
  msg = poly.create(0b001111101110, 12)
  w = golay.encode(msg)
  assert np.equal(w, poly.create(0b001111101110_010010010010, 24)).all()
  w = poly.create(0b101111101111_010010010010, 24)
  v = golay.decode(w)
  assert np.equal(v, poly.create(0b001111101110_010010010010, 24)).all()


def test_2():
  w = poly.create(0b001001001101_101000101000, 24)
  v = golay.decode(w)
  assert np.equal(v, poly.create(0b001001011111_101010101000, 24)).all()


def test_3():
  w = poly.create(0b000111000111_011011010000, 24)
  v = golay.decode(w)
  assert np.equal(v, poly.create(0b000011000111_011010000000, 24)).all()


test_1()
test_2()
test_3()