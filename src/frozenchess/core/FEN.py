from __future__ import annotations

import operator
from typing import *

import keyalias
from normedtuple import normedtuple

from frozenchess.bases import *
from frozenchess.core.Castle import Castle
from frozenchess.core.Piece import Piece
from frozenchess.core.Placement import Placement
from frozenchess.core.Square import Square

__all__ = ["FEN"]


@normedtuple
def BaseFEN(
    cls: type,
    other: Optional[Iterable] = None,
    /,
    *,
    placement: Optional[Placement] = None,
    turn: Optional[Piece.Color] = None,
    castle: Optional[Castle] = None,
    ep: Optional[Square] = None,
    halfmoveClock: Optional[int] = None,
    fullmoveNumber: Optional[int] = None,
):
    p: Any = None
    t: Any = None
    c: Any = None
    e: Any = None
    h: Any = None
    f: Any = None
    if other is not None:
        p, t, c, e, h, f = other
    if placement is not None:
        p = placement
    if turn is not None:
        t = turn
    if castle is not None:
        c = castle
    if ep is not None:
        e = ep
    if halfmoveClock is not None:
        h = halfmoveClock
    if fullmoveNumber is not None:
        f = fullmoveNumber
    p = Placement(p)
    t = Piece.Color.WHITE if p is None else Piece.Color(t)
    c = Castle.byPlacement(p) if c is None else Castle(c)
    e = Square.A1 if e is None else Square(e)
    h = 0 if h is None else operator.index(h)
    f = 1 if h is None else operator.index(f)
    return [p, t, c, e, h, f]


@keyalias.getdecorator(
    placement=0,
    turn=1,
    castle=2,
    ep=3,
    halfmoveClock=4,
    fullmoveNumber=5,
)
class FEN(BaseFEN, FENStylable, Mirrorable, Starting):
    @classmethod
    def byFENStyled(cls: type, /, styled: Any) -> Self:
        s: str = str(styled)
        parts: list = s.split()
        parts[0] = Placement.byFENStyled(parts[0])
        parts[1] = Piece.Color.byFENStyled(parts[1])
        parts[2] = Castle.byFENStyled(parts[2])
        parts[3] = Square.byFENStyled(parts[3])
        parts[4] = int(parts[4])
        parts[5] = int(parts[5])
        ans: Self = cls(parts)
        return ans

    def fenStyled(self: Self, /) -> str:
        l: list = list()
        l.append(self.placement.fenStyled())
        l.append(self.turn.fenStyled())
        l.append(self.castle.fenStyled())
        l.append(self.ep.fenStyled())
        l.append(int(self.halfmoveClock))
        l.append(int(self.fullmoveNumber))
        ans: str = " ".join(l)
        return ans

    def mirror(self: Self, /) -> Self:
        l: list = list(self)
        i: int = 0
        for i in range(4):
            l[i] = l[i].mirror()
        ans: Self = type(self)(l)
        return ans

    @classmethod
    def starting(cls: type) -> Self:
        return cls(None, placement=Placement.starting())
