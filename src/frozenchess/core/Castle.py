from __future__ import annotations

from typing import *

from frozenchess.bases import *
from frozenchess.core.Piece import Piece
from frozenchess.core.Placement import Placement
from frozenchess.core.Square import Square

__all__ = ["Castle"]


class Castle(Mirrorable, Starting, Flag):
    NONE = 0
    WHITE_KINGSIDE = 1
    WHITE_QUEENSIDE = 2
    BLACK_KINGSIDE = 4
    BLACK_QUEENSIDE = 8
    ALL = 15

    @classmethod
    def _mod(cls: type, /) -> int:
        return 16

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

    def mirror(self: Self, /) -> Self:
        ans: Self = type(self).NONE
        if self & type(self).WHITE_KINGSIDE:
            ans |= type(self).BLACK_KINGSIDE
        if self & type(self).WHITE_QUEENSIDE:
            ans |= type(self).BLACK_QUEENSIDE
        if self & type(self).BLACK_KINGSIDE:
            ans |= type(self).WHITE_KINGSIDE
        if self & type(self).BLACK_QUEENSIDE:
            ans |= type(self).WHITE_QUEENSIDE
        return ans

    @classmethod
    def starting(cls: type, /) -> Self:
        return cls.ALL


def setup() -> None:
    Castle.NONE._fen = "-"
    for n in range(1, 16):
        x = Castle(n)
        x._fen = ""
        if x & Castle.WHITE_KINGSIDE:
            x._fen += "K"
        if x & Castle.WHITE_QUEENSIDE:
            x._fen += "Q"
        if x & Castle.BLACK_KINGSIDE:
            x._fen += "k"
        if x & Castle.BLACK_QUEENSIDE:
            x._fen += "q"


setup()
