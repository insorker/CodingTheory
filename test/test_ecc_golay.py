import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import random
from src.ecc.golay import *
from src.galois.poly import *
import src.channel.common as channel


golay = Golay_24_12_8()


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


def test_rand():
  n, k = 24, 12
  
  for i in range(0, 1000):
    msg_send = channel.message(k)
    codeword_send = golay.encode(msg_send)
    noise = channel.noise(n, random.randint(0, 3))
    codeword_recv = poly.add(codeword_send, noise)
    msg_recv = golay.decode(codeword_recv)
    if not np.array_equal(msg_send, msg_recv):
      print(i)
      print(msg_send)
      print(msg_recv)
      assert False


# test_1()
# test_2()
# test_3()
test_rand()