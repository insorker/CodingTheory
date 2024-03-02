import numpy as np


def cstyle_vec(vec: np.ndarray, name: str):
  r, = vec.shape
  return \
f"""int {name}[{r}] = {{{','.join(map(str, vec))}}};"""


def cstyle_mt(mt: np.ndarray, name: str):
  r, c = mt.shape
  return \
f"""int {name}[{r}][{c}] = {{
  {map(str, [','.join(map(str, mt[i])) + ',' if i != r - 1 else ' ' for i in range(0, r)])}
}};"""