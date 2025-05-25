import enum
import operator
from typing import *

from frozenchess.bases.ables.SubInt import *

__all__ = ["Mod"]


class Mod(SubInt, enum.Enum):
    @classmethod
    def _missing_(cls: type, /, value: SupportsIndex) -> Self:
        i: int = operator.index(value) % len(cls)
        ans: Self = cls(i)
        return ans
