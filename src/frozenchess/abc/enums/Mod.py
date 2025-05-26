import enum
import operator
from typing import *

import cooltypes

from frozenchess.abc.enums.Meta import *

__all__ = ["Mod"]


class Mod(cooltypes.CoolInt, enum.Enum, metaclass=Meta):
    @classmethod
    def _missing_(cls: type, /, value: SupportsIndex) -> Self:
        i: int = operator.index(value) % len(cls)
        ans: Self = cls(i)
        return ans
