from __future__ import annotations

from typing import *

import chess
from normedtuple import normedtuple

from frozenchess.bases import *
from frozenchess.core.Piece import Piece
from frozenchess.core.Square import Square

__all__ = ["Placement"]


@normedtuple
def BasePlacement(
    cls: type,
    other: Optional[Iterable] = None,
    /,
    **kwargs: Optional[Piece],
) -> list:
    ans: list = [None] * 64
    if other is not None:
        ans = list(other)
        if len(ans) > 64:
            raise ValueError(other)
    k: str = ""
    v: Any = None
    for k, v in kwargs.items():
        s: Square = Square[k.upper()]
        ans[s] = v
    i: int
    for i in range(64):
        if ans[i] is None:
            continue
        ans[i] = Piece(ans[i])
    return ans


class Placement(BasePlacement, Starting):
    @classmethod
    def byFENStyled(cls: type, /, styled: Any) -> Self:
        full_fen: str = str(styled) + " w - - 0 1"
        board: chess.Board = chess.Board(full_fen)
        data: list = list()
        p: Any = None
        for i in range(64):
            x: Any = board.piece_at(i)
            if x:
                s: Any = x.symbol()
                p = Piece.byFENStyled(s)
            else:
                p = None
            data.append(p)
        ans: Self = cls(data)
        return ans

    def fenStyled(self: Self, /) -> str:
        fenRows: list = []
        for rank in range(8, 0, -1):
            row: str = ""
            empty: int = 0
            for file in range(8):
                i: int = rank * 8 + file - 8
                piece: Optional[Piece] = self[i]
                if piece is None:
                    empty += 1
                    continue
                if empty > 0:
                    row += str(empty)
                    empty = 0
                row += piece.fenStyled()
            if empty > 0:
                row += str(empty)
            fenRows.append(row)

        return "/".join(fenRows)

    def mirror(self: Self, /) -> Self:
        "This method swaps the players."
        return type(self)(reversed(self))

    @classmethod
    def starting(cls: type, /) -> Self:
        return cls.byFENStyled("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR")
