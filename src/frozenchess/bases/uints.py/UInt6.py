from typing import *

from frozenchess.bases.uints.UIntBase import *

__all__ = ["UInt6"]


class UInt6(UIntBase):
    @classmethod
    def modulus(cls: type, /) -> int:
        return 64
