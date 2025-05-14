from __future__ import annotations

import enum
from typing import *

from frozenchess.bases.AbstractionError import *
from frozenchess.bases.FENStylable import *
from frozenchess.bases.Mod import *

__all__ = ["IntMod"]


class IntMod(FENStylable, Mod):

    @classmethod
    def byFENStyled(cls: type, styled: Any) -> Self:
        fen: str = str(styled)
        for x in cls:
            if x._fen == fen:
                return x
        raise ValueError(styled)

    def fenStyled(self: Self) -> str:
        return self._fen
