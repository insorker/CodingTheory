from src.ecc.base import *
import src.galois.poly as poly
import src.channel.common as channel


def test_auto_overall(n: int, k: int, t: int, ecc: EccBase):
  """Automated testing for all procedures.

  Args:
      n (int): length of codeword
      k (int): length of message
      t (int): number of errors
      ecc (EccBase): ecc model
  """
  msg = channel.it_message(k)

  for i in range(channel.it_message_size(k)):
    m0 = next(msg)
    c0 = ecc.encode(m0)
    assert len(c0) == n, f"Encode Error: length ({len(c0), n}) dismatch."

    for j in range(t + 1):
      noise = channel.it_noise(n, j)

      for l in range(channel.it_noise_size(n, j)):
        c1 = poly.add(c0, next(noise))
        m1 = ecc.decode(c1)
        assert len(m1) == k, f"Decode Error: length ({len(m1), k}) dismatch."

        if not np.array_equal(m0, m1):
          print(f"Step({i, j, l}):")
          print(f"m0: {m0}")
          print(f"c0: {c0}")
          print(f"c1: {c1}")
          print(f"m1: {m1}")
          assert False


def test_auto_rand(n: int, k: int, t: int, ecc: EccBase, times: tuple = (100, 100)):
  """Automated testing for random procedures, repeated `times[0]` * `times[1]` times.

  Args:
      n (int): length of codeword
      k (int): length of message
      t (int): number of errors
      ecc (EccBase): ecc model
      times (tuple): (number of random messages, number of random noises)
  """
  for i in range(times[0]):
    m0 = channel.message(k)
    c0 = ecc.encode(m0)
    assert len(c0) == n, f"Encode Error: length ({len(c0), n}) dismatch."

    for j in range(t + 1):
      for l in range(times[1]):
        c1 = poly.add(c0, channel.noise(n, j))
        m1 = ecc.decode(c1)
        assert len(m1) == k, f"Decode Error: length ({len(m1), k}) dismatch."

        if not np.array_equal(m0, m1):
          print(f"Step({i, j, l}):")
          print(f"m0: {m0}")
          print(f"c0: {c0}")
          print(f"c1: {c1}")
          print(f"m1: {m1}")
          assert False