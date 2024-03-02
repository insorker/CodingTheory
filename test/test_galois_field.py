import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.galois import field


def test_print(gf):
  for i in range(0, 1 << gf.m):
    print("{}\t{}".format(i, bin(gf.e2v(i))[2:].zfill(gf.m)))
  print()
  for i in range(0, 1 << gf.m):
    print("{}\t{}".format(bin(i)[2:].zfill(gf.m), gf.v2e(i)))


def test_5():
  gf = field.Field(5, 0b100101)
  test_print(gf)
  print(gf.cstyle())


test_5()
