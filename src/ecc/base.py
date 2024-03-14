from abc import ABC, abstractmethod
from src.galois.type import *


class EccBase(ABC):
  @abstractmethod
  def encode(self, msg: PolyLike) -> PolyLike:
    pass

  @abstractmethod
  def decode(self, msg: PolyLike) -> PolyLike:
    pass