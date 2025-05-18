import enum
import operator
from typing import *

__all__ = ["Mod"]


class Mod(enum.IntEnum):
    @classmethod
    def _missing_(cls: type, /, value: SupportsIndex) -> Self:
        i: int = operator.index(value) % len(cls)
        ans: Self = cls(i)
        return ans
