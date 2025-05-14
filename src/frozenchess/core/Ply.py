from __future__ import annotations

from typing import *

import keyalias
from normedtuple import normedtuple

from frozenchess.bases import *
from frozenchess.core.Piece import Piece
from frozenchess.core.Square import Square

__all__ = ["Ply"]

EMPTY: tuple = (0, 0, Piece.Kind.PAWN)


@normedtuple
def BasePly(
    cls: type,
    other: Optional[Iterable] = None,
    /,
    *,
    start: Optional[Square] = None,
    stop: Optional[Square] = None,
    promotion: Optional[Piece.Kind] = None,
) -> tuple:
    if {other, start, stop, promotion} == {None}:
        return EMPTY
    a: Any = None
    b: Any = None
    c: Any = Piece.Kind.PAWN
    if other is not None:
        a, b, c = other
    if start is not None:
        a = start
    if stop is not None:
        b = stop
    if promotion is not None:
        c = promotion
    a = Square(a)
    b = Square(b)
    c = Piece.Kind(c)
    return a, b, c


@keyalias.getdecorator(start=0, stop=1, promotion=2)
class Ply(BasePly, Mirrorable, UCIStylable):
    @classmethod
    def byUCIStyled(cls: type, /, styled: Any) -> Self:
        s: str = str(styled)
        a: str = s[:2]
        b: str = s[2:4]
        c: str = s[4:]
        x: Square = Square.byUCIStyled(a)
        y: Square = Square.byUCIStyled(b)
        z: Piece.Kind = Piece.Kind.byUCIStyled(c)
        ans: Self = cls([x, y, z])
        return ans

    def isempty(self: Self, /) -> bool:
        return self == EMPTY

    def mirror(self: Self, /) -> Self:
        "This method swaps the players."
        a: Square = self.start
        b: Square = self.stop
        if a != b:
            a = a.mirror()
            b = b.mirror()
        return type(self)([a, b, self.promotion])
