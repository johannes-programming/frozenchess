from __future__ import annotations

from enum import IntEnum
from typing import *

import keyalias
from normedtuple import normedtuple

__all__ = ["Piece"]


@normedtuple
def BasePiece(
    cls: type,
    other: Optional[Iterable] = None,
    /,
    *,
    color: Optional[Color] = None,
    kind: Optional[Kind] = None,
) -> list:
    c: Any = None
    k: Any = None
    if other is not None:
        c, k = other
    if color is not None:
        c = color
    if kind is not None:
        k = kind
    c = Color(c)
    k = Kind(k)
    return c, k


class Color(IntEnum):
    WHITE = True
    BLACK = False

    def mirror(self) -> Self:
        "This method swaps the players."
        return type(self)(1 - self)


class Kind(IntEnum):
    PAWN = 1
    KNIGHT = 2
    BISHOP = 3
    ROOK = 4
    QUEEN = 5
    KING = 6


@keyalias.getdecorator(color=0, kind=1)
class Piece(BasePiece):
    def mirror(self) -> Self:
        "This method swaps the players."
        c: Color = self.color.mirror()
        k: Kind = self.kind
        ans: Self = type(self)(color=c, kind=k)
        return ans


Piece.Color = Color
Piece.Kind = Kind
