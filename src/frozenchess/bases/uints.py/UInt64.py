from typing import *

from frozenchess.bases.uints.UIntBase import *

__all__ = ["UInt64"]


class UInt64(UIntBase):
    @classmethod
    def modulus(cls: type, /) -> int:
        return 18446744073709551616
