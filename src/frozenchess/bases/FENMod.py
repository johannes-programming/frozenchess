from __future__ import annotations

from typing import *

from frozenchess.bases.AbstractionError import *
from frozenchess.bases.FENStylable import *
from frozenchess.bases.Mod import *

__all__ = ["FENMod"]


class FENMod(Mod, FENStylable):

    @classmethod
    def byFENStyled(cls: type, /, styled: Any) -> Self:
        fen: str = str(styled)
        for x in cls:
            if x._fen == fen:
                return x
        raise ValueError(styled)

    def fenStyled(self: Self, /) -> str:
        return self._fen
