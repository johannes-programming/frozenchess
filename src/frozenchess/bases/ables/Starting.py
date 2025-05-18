from typing import *

from frozenchess.bases.abstraction import *

__all__ = ["Starting"]


class Starting:
    @classmethod
    def starting(cls: type, /) -> Self:
        raise AbstractionError
