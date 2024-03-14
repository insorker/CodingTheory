import numpy as np


ExpLike = int
"""exponent, 幂表示: int

e.g.
  a^0  <=>  0;
  a^1  <=>  1;
  a^2  <=>  2;
  a^12 <=> 12;
"""


VecLike = int
"""vector, 向量表示: int

e.g.
  0001 <=>  1;
  0010 <=>  2;
  0100 <=>  4;
  1111 <=> 15;
"""


PolyLike = np.ndarray
"""polynomial, 多项式表示: np.ndarray

e.g.
                  1 <=> [0, 0, 0, 1];
              a     <=> [0, 0, 1, 0];
        a^2         <=> [0, 1, 0, 0];
  a^3 + a^2 + a + 1 <=> [1, 1, 1, 1];
"""
