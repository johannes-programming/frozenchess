from __future__ import annotations

from enum import IntFlag
from typing import *

from normedtuple import normedtuple

from frozenchess.core.Piece import Piece
from frozenchess.core.Placement import Placement
from frozenchess.core.Square import Square

__all__ = ["CastlingAvailability"]


class CastlingAvailability(IntFlag):
    

@normedtuple
def BaseCastlingAvailability(
    cls: type, 
    other: Optional[Iterable] = None, /, *, 
    placement:Optional[Placement] = None, 
    turn:Optional[Piece.Color] = None,
    

) -> list:
    ans: list = [None] * 64
    if other is not None:
        ans = list(other)
        if len(ans) > 64:
            raise ValueError(other)
    k: str
    v: Any
    for k, v in kwargs.items():
        s: Square = Square[k.upper()]
        ans[s] = v
    i: int
    for i in range(64):
        if ans[i] is None:
            continue
        ans[i] = Piece(ans[i])
    return ans


class Placement(BasePlacement):
    def mirror(self) -> Self:
        "This method swaps the players."
        return type(self)(reversed(self))
