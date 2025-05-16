from typing import *

from frozenchess.bases.AbstractionError import *

__all__ = ["FENStylable"]


class FENStylable:
    @classmethod
    def byFENStyled(cls: type, /, styled: Any) -> Self:
        raise AbstractionError

    def fenStyled(self: Self, /) -> str:
        raise AbstractionError
