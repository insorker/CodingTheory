import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import numpy as np
from src.ecc.bch import *
from src.galois.field import *
import src.channel.common as channel


def test_hamming_code():
  n, k, d, t, g = 15, 11, 3, 1, 0b10011
  m, prim = 4, 0b10011
  bch = BCH(n, k, d, t, Field(m, prim), g)

  msg = channel.it_message(k)
  for _ in range(0, channel.it_message_size(k)):
    msg_send = next(msg)
    codeword_send = bch.encode(msg_send)

    noise = channel.it_noise(n, t)
    for i in range(0, channel.it_noise_size(n, t)):
      codeword_recv = poly.add(codeword_send, next(noise))
      msg_recv = bch.decode_t1(codeword_recv)
      if not np.array_equal(msg_send, msg_recv):
        print(msg_send)
        print(msg_recv)
        assert False


test_hamming_code()