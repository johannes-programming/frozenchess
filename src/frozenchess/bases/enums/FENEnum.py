from __future__ import annotations

from enum import Enum
from typing import *

from frozenchess.bases.ables import *
from frozenchess.bases.abstraction import *

__all__ = ["FENEnum"]


class FENEnum(FENStylable, Enum):

    @classmethod
    def byFENStyled(cls: type, /, styled: Any) -> Self:
        fen: str = str(styled)
        for x in cls:
            if x._fen == fen:
                return x
        raise ValueError(styled)

    def fenStyled(self: Self, /) -> str:
        return self._fen
