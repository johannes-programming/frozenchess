from typing import *

from frozenchess.bases.uints.UIntBase import *

__all__ = ["UInt1"]


class UInt1(UIntBase):
    @classmethod
    def modulus(cls: type, /) -> int:
        return 2
