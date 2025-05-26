from __future__ import annotations

from typing import *

from frozenchess.abc import *
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


class File(HasNative, Mod):
    "This enum represents the files of the chessboard."

    A = 0
    B = 1
    C = 2
    D = 3
    E = 4
    F = 5
    G = 6
    H = 7

    def native(self: Self, /) -> Piece.Kind:
        "This method returns the native of the instance."
        return _NATIVES[self]
