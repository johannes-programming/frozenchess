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


class File(Starting, Flag, metaclass=FlagMeta):
    (
        A,
        B,
        C,
        D,
        E,
        F,
        G,
        H,
    ) = range(8)

    @classmethod
    def _mod(cls) -> int:
        return 8

    def starting(self) -> Piece.Kind:
        return _NATIVES[self]
