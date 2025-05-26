from __future__ import annotations

from typing import *

from frozenchess.abc import *
from frozenchess.core.Piece import *
from frozenchess.core.Placement import *
from frozenchess.core.Square import *

__all__ = ["Castle"]


class Castle(FENStylable, Mirrorable, Starting, Flag):
    NONE = 0
    WHITE_KINGSIDE = 1
    WHITE_QUEENSIDE = 2
    BLACK_KINGSIDE = 4
    BLACK_QUEENSIDE = 8
    ALL = 15

    @classmethod
    def byFENStyled(cls: type, /, styled: Any) -> Self:
        s: str = str(styled)
        if s == "-":
            return cls(0)
        n: int = 0
        for i, x in enumerate("KQkq"):
            if s.startswith(x):
                n += 2**i
        ans: Self = cls(n)
        return ans

    @classmethod
    def byPlacement(cls: type, /, placement: Placement) -> Self:
        p: Placement = Placement(placement)
        a1 = p[Square.A1] == Piece.byFENStyled("R")
        e1 = p[Square.E1] == Piece.byFENStyled("K")
        h1 = p[Square.H1] == Piece.byFENStyled("R")
        a8 = p[Square.A8] == Piece.byFENStyled("r")
        e8 = p[Square.E8] == Piece.byFENStyled("k")
        h8 = p[Square.H8] == Piece.byFENStyled("r")
        ans: Self = cls.NONE
        if a1 and e1:
            ans &= cls.WHITE_QUEENSIDE
        if h1 and e1:
            ans &= cls.WHITE_KINGSIDE
        if a8 and e8:
            ans &= cls.BLACK_QUEENSIDE
        if h8 and e8:
            ans &= cls.BLACK_KINGSIDE
        return ans

    def fenStyled(self: Self, /) -> str:
        if self == 0:
            return "-"
        ans: str = ""
        for i, x in enumerate("KQkq"):
            if (2**i) & self:
                ans += x
        return ans

    def mirror(self: Self, /) -> Self:
        n: int = (self << 2) | (self >> 2)
        ans: Self = type(self)(n)
        return ans

    @classmethod
    def starting(cls: type, /) -> Self:
        return cls.ALL
