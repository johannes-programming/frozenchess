from __future__ import annotations

import enum
from typing import *

from frozenchess.bases import *
from frozenchess.core.Piece import Piece

__all__ = ["File"]

_NATIVES = [
    Piece.Kind.ROOK,
    Piece.Kind.KNIGHT,
    Piece.Kind.BISHOP,
    Piece.Kind.QUEEN,
    Piece.Kind.KING,
    Piece.Kind.BISHOP,
    Piece.Kind.KNIGHT,
    Piece.Kind.ROOK,
]


class File(Starting, Mod):
    A = 0
    B = 1
    C = 2
    D = 3
    E = 4
    F = 5
    G = 6
    H = 7

    def starting(self: Self, /) -> Piece.Kind:
        return _NATIVES[self]
