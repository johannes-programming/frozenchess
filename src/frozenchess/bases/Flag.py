from __future__ import annotations

import enum
from typing import *

from frozenchess.bases.AbstractionError import *
from frozenchess.bases.FENStylable import *

__all__ = ["Flag"]


class Flag(FENStylable, enum.IntFlag):
    @classmethod
    def _mod(cls: type) -> int:
        raise AbstractionError

    @classmethod
    def byFENStyled(cls: type, styled: Any) -> Self:
        fen: str = str(styled)
        for x in cls:
            if x._fen == fen:
                return x
        raise ValueError(styled)

    def fenStyled(self: Self) -> str:
        return self._fen
