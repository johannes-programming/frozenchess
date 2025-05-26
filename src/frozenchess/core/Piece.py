from __future__ import annotations

import enum
from typing import *

from frozenchess import _utils
from frozenchess.abc import *

__all__ = ["Piece"]


class Color(FENStylable, Mirrorable, Mod):
    WHITE = True
    BLACK = False

    @classmethod
    def byFENStyled(cls: type, /, styled: Any) -> Any:
        return dict(b=0, w=1)[str(styled)]

    def fenStyled(self: Self, /) -> str:
        return "bw"[self]

    def mirror(self: Self, /) -> Self:
        "This method swaps the players."
        return type(self)(1 - self)


class Kind(UCIStylable, Token):
    PAWN = ""
    KNIGHT = "N"
    BISHOP = "B"
    ROOK = "R"
    QUEEN = "Q"
    KING = "K"

    @classmethod
    def byUCIStyled(cls: type, /, styled: Any) -> Self:
        s: str = str(styled)
        if s == "K":
            raise ValueError(styled)
        ans: Self = cls(s)
        return ans

    def uciStyled(self: Self, /) -> str:
        return self.value


@_utils.tuplize
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


class Piece(BasePiece, FENStylable, Mirrorable):
    @classmethod
    def byFENStyled(cls: type, /, styled: Any) -> Self:
        return cls._ANTIFEN[str(styled)]

    def fenStyled(self: Self, /) -> str:
        return type(self)._FEN[self]

    def mirror(self: Self, /) -> Self:
        "This method swaps the players."
        c: Color = self.color.mirror()
        k: Kind = self.kind
        ans: Self = type(self)(color=c, kind=k)
        return ans


def setup() -> None:
    Piece.Color = Color
    Piece.Kind = Kind
    Piece._ANTIFEN = {
        "P": Piece(color=Color.WHITE, kind=Kind.PAWN),
        "N": Piece(color=Color.WHITE, kind=Kind.KNIGHT),
        "B": Piece(color=Color.WHITE, kind=Kind.BISHOP),
        "R": Piece(color=Color.WHITE, kind=Kind.ROOK),
        "Q": Piece(color=Color.WHITE, kind=Kind.QUEEN),
        "K": Piece(color=Color.WHITE, kind=Kind.KING),
        "p": Piece(color=Color.BLACK, kind=Kind.PAWN),
        "n": Piece(color=Color.BLACK, kind=Kind.KNIGHT),
        "b": Piece(color=Color.BLACK, kind=Kind.BISHOP),
        "r": Piece(color=Color.BLACK, kind=Kind.ROOK),
        "q": Piece(color=Color.BLACK, kind=Kind.QUEEN),
        "k": Piece(color=Color.BLACK, kind=Kind.KING),
    }
    Piece._FEN = _utils.antidict(Piece._ANTIFEN)


setup()
