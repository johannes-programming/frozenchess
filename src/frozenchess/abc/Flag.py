from __future__ import annotations

import enum
from typing import *

from frozenchess.abc.FENStylable import FENStylable
from frozenchess.abc.FlagMeta import FlagMeta

__all__ = ["Flag"]


class BaseFlag(metaclass=FlagMeta): ...


class Flag(BaseFlag, enum.IntFlag, FENStylable):
    # overwrites
    @classmethod
    def byFENStyled(cls, styled: Any) -> Self:
        fen: str = str(styled)
        for x in cls:
            if x._fen == fen:
                return x
        raise ValueError(styled)

    def fenStyled(self) -> str:
        return self._fen
