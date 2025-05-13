from __future__ import annotations

from typing import *

from frozenchess.abc import *
from frozenchess.core.File import File
from frozenchess.core.Piece import Piece

__all__ = ["Square"]


class Color(Flag):
    LIGHT = True
    DARK = False

    def mirror(self) -> Self:
        "This method swaps the players."
        return -self


class Square(Flag):  # , Mirrorable, UCIStylable, Starting):

    (
        A1,
        B1,
        C1,
        D1,
        E1,
        F1,
        G1,
        H1,
        A2,
        B2,
        C2,
        D2,
        E2,
        F2,
        G2,
        H2,
        A3,
        B3,
        C3,
        D3,
        E3,
        F3,
        G3,
        H3,
        A4,
        B4,
        C4,
        D4,
        E4,
        F4,
        G4,
        H4,
        A5,
        B5,
        C5,
        D5,
        E5,
        F5,
        G5,
        H5,
        A6,
        B6,
        C6,
        D6,
        E6,
        F6,
        G6,
        H6,
        A7,
        B7,
        C7,
        D7,
        E7,
        F7,
        G7,
        H7,
        A8,
        B8,
        C8,
        D8,
        E8,
        F8,
        G8,
        H8,
    ) = range(64)

    @classmethod
    def byUCIStyled(cls, styled: Any) -> Self:
        s: str = str(styled)
        for x in cls:
            if x.name.lower() == s:
                return x
        raise ValueError(styled)

    def color(self) -> Color:
        return Color(self % 2)

    def file(self) -> File:
        return File(self // 8)

    def mirror(self) -> Self:
        "This method swaps the players."
        r: int = 9 - self.rank()
        n: str = self.file().name + str(r)
        ans: Self = type(self)[n]
        return ans

    def starting(self) -> Piece:
        return self._NATIVE

    def rank(self) -> int:
        return (self // 8) + 1

    def uciStyled(self) -> str:
        return self.name.lower()


def setup_getnative(square: Square) -> Piece:
    ans: Optional[Piece] = None
    rank: int = square.rank()
    kind: Piece.Kind = square.file().starting()
    if rank == 1:
        ans = Piece(color=Piece.Color.WHITE, kind=kind)
    elif rank == 2:
        ans = Piece(color=Piece.Color.WHITE, kind=Piece.Kind.PAWN)
    elif rank == 7:
        ans = Piece(color=Piece.Color.BLACK, kind=Piece.Kind.PAWN)
    elif rank == 8:
        ans = Piece(color=Piece.Color.BLACK, kind=kind)
    return ans


def setup() -> None:
    Square.Color = Color

    for x in Square:
        x._NATIVE = setup_getnative(x)
        if x:
            x._fen = x.name.lower()
        else:
            x._fen = "-"
        x._uci = x.name.lower()


setup()
