from __future__ import annotations

from typing import *

from frozenchess.bases import *
from frozenchess.core.File import File
from frozenchess.core.Piece import Piece

__all__ = ["Square"]


class Color(Flag):
    LIGHT = True
    DARK = False

    def mirror(self: Self, /) -> Self:
        "This method swaps the players."
        return ~self


class Square(Mirrorable, Starting, UCIStylable, Flag):

    A1 = 0
    B1 = 1
    C1 = 2
    D1 = 3
    E1 = 4
    F1 = 5
    G1 = 6
    H1 = 7
    A2 = 8
    B2 = 9
    C2 = 10
    D2 = 11
    E2 = 12
    F2 = 13
    G2 = 14
    H2 = 15
    A3 = 16
    B3 = 17
    C3 = 18
    D3 = 19
    E3 = 20
    F3 = 21
    G3 = 22
    H3 = 23
    A4 = 24
    B4 = 25
    C4 = 26
    D4 = 27
    E4 = 28
    F4 = 29
    G4 = 30
    H4 = 31
    A5 = 32
    B5 = 33
    C5 = 34
    D5 = 35
    E5 = 36
    F5 = 37
    G5 = 38
    H5 = 39
    A6 = 40
    B6 = 41
    C6 = 42
    D6 = 43
    E6 = 44
    F6 = 45
    G6 = 46
    H6 = 47
    A7 = 48
    B7 = 49
    C7 = 50
    D7 = 51
    E7 = 52
    F7 = 53
    G7 = 54
    H7 = 55
    A8 = 56
    B8 = 57
    C8 = 58
    D8 = 59
    E8 = 60
    F8 = 61
    G8 = 62
    H8 = 63

    @classmethod
    def byUCIStyled(cls: type, /, styled: Any) -> Self:
        s: str = str(styled)
        for x in cls:
            if x.name.lower() == s:
                return x
        raise ValueError(styled)

    def color(self: Self, /) -> Color:
        return Color(self % 2)

    def file(self: Self, /) -> File:
        return File(self // 8)

    def mirror(self: Self, /) -> Self:
        "This method swaps the players."
        r: int = 9 - self.rank()
        n: str = self.file().name + str(r)
        ans: Self = type(self)[n]
        return ans

    def starting(self: Self, /) -> Piece:
        return self._NATIVE

    def rank(self: Self, /) -> int:
        return (self // 8) + 1

    def uciStyled(self: Self, /) -> str:
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
