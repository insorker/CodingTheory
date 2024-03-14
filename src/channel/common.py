import numpy as np
import random
from typing import Iterator
import math
import src.galois.poly as poly
from src.galois.type import *


def message(length: int) -> PolyLike:
  """Return random messgae.
  """
  return np.array([random.randint(0, 1) for _ in range(0, length)], dtype=int)


def noise(length: int, err_cnt: int) -> PolyLike:
  """Return random noise.
  """
  res = np.zeros(length, dtype=int)
  err_idx = random.sample(range(0, length), err_cnt)
  for i in err_idx:
    res[i] = 1
  return res


def it_message_size(length: int) -> int:
  """Maximum number of message iterations.
  """
  return 1 << length


def it_message(length: int) -> Iterator[PolyLike]:
  """Iterate all messages.
  """
  vec = -1
  while vec < it_message_size(length) - 1:
    vec += 1
    yield poly.create(vec, length)


def it_noise_size(n: int, k: int) -> int:
  """Maximum number of noise iterations.
  """
  return math.perm(n, k)


def it_noise(length: int, err_cnt: int) -> Iterator[PolyLike]:
  """Iterate all noises.
  """
  def it_noise_dfs(depth: int, left: int):
    if left == 0 or depth == length:
      yield result
    elif length - depth >= left:
      yield from it_noise_dfs(depth + 1, left)
      result[depth] = 1
      yield from it_noise_dfs(depth + 1, left - 1)
      result[depth] = 0

  result = np.zeros(length, dtype=int)
  yield from it_noise_dfs(0, err_cnt)