from typing import *

from frozenchess.bases.AbstractionError import *

__all__ = ["UCIStylable"]


class UCIStylable:
    @classmethod
    def byUCIStyled(cls: type, /, styled: Any) -> Self:
        raise AbstractionError

    def uciStyled(self: Self, /) -> str:
        raise AbstractionError
