from __future__ import annotations

from typing import *

import chess

from frozenchess import _utils
from frozenchess.abc import *
from frozenchess.core.BitBoard import *
from frozenchess.core.Piece import Piece
from frozenchess.core.Square import Square

__all__ = ["Placement"]


@_utils.tuplize
def BasePlacement(
    cls: type,
    other: Optional[Iterable] = None,
    /,
    a1: Optional[Piece] = None,
    b1: Optional[Piece] = None,
    c1: Optional[Piece] = None,
    d1: Optional[Piece] = None,
    e1: Optional[Piece] = None,
    f1: Optional[Piece] = None,
    g1: Optional[Piece] = None,
    h1: Optional[Piece] = None,
    a2: Optional[Piece] = None,
    b2: Optional[Piece] = None,
    c2: Optional[Piece] = None,
    d2: Optional[Piece] = None,
    e2: Optional[Piece] = None,
    f2: Optional[Piece] = None,
    g2: Optional[Piece] = None,
    h2: Optional[Piece] = None,
    a3: Optional[Piece] = None,
    b3: Optional[Piece] = None,
    c3: Optional[Piece] = None,
    d3: Optional[Piece] = None,
    e3: Optional[Piece] = None,
    f3: Optional[Piece] = None,
    g3: Optional[Piece] = None,
    h3: Optional[Piece] = None,
    a4: Optional[Piece] = None,
    b4: Optional[Piece] = None,
    c4: Optional[Piece] = None,
    d4: Optional[Piece] = None,
    e4: Optional[Piece] = None,
    f4: Optional[Piece] = None,
    g4: Optional[Piece] = None,
    h4: Optional[Piece] = None,
    a5: Optional[Piece] = None,
    b5: Optional[Piece] = None,
    c5: Optional[Piece] = None,
    d5: Optional[Piece] = None,
    e5: Optional[Piece] = None,
    f5: Optional[Piece] = None,
    g5: Optional[Piece] = None,
    h5: Optional[Piece] = None,
    a6: Optional[Piece] = None,
    b6: Optional[Piece] = None,
    c6: Optional[Piece] = None,
    d6: Optional[Piece] = None,
    e6: Optional[Piece] = None,
    f6: Optional[Piece] = None,
    g6: Optional[Piece] = None,
    h6: Optional[Piece] = None,
    a7: Optional[Piece] = None,
    b7: Optional[Piece] = None,
    c7: Optional[Piece] = None,
    d7: Optional[Piece] = None,
    e7: Optional[Piece] = None,
    f7: Optional[Piece] = None,
    g7: Optional[Piece] = None,
    h7: Optional[Piece] = None,
    a8: Optional[Piece] = None,
    b8: Optional[Piece] = None,
    c8: Optional[Piece] = None,
    d8: Optional[Piece] = None,
    e8: Optional[Piece] = None,
    f8: Optional[Piece] = None,
    g8: Optional[Piece] = None,
    h8: Optional[Piece] = None,
) -> list:
    ans: list = [None] * 64
    if other is not None:
        ans = list(other)
        if len(ans) > 64:
            raise ValueError(other)
    exp: list = [
        a1,
        b1,
        c1,
        d1,
        e1,
        f1,
        g1,
        h1,
        a2,
        b2,
        c2,
        d2,
        e2,
        f2,
        g2,
        h2,
        a3,
        b3,
        c3,
        d3,
        e3,
        f3,
        g3,
        h3,
        a4,
        b4,
        c4,
        d4,
        e4,
        f4,
        g4,
        h4,
        a5,
        b5,
        c5,
        d5,
        e5,
        f5,
        g5,
        h5,
        a6,
        b6,
        c6,
        d6,
        e6,
        f6,
        g6,
        h6,
        a7,
        b7,
        c7,
        d7,
        e7,
        f7,
        g7,
        h7,
        a8,
        b8,
        c8,
        d8,
        e8,
        f8,
        g8,
        h8,
    ]
    i: int = -1
    for i in range(64):
        if exp[i] is not None:
            ans[i] = exp[i]
        if ans[i] is not None:
            ans[i] = Piece(ans[i])
    return ans


class Placement(BasePlacement, FENStylable, Mirrorable, Starting):
    def bitBoard(self: Self, /, *args: None | Iterable) -> BitBoard:
        opts = set()
        for a in args:
            if a is None:
                opts.add(None)
            else:
                opts.add(Piece(a))
        n: int = 0
        for i in range(64):
            if self[i] in opts:
                n |= 2**i
        ans: BitBoard = BitBoard(n)
        return ans

    @classmethod
    def byFENStyled(cls: type, /, styled: Any) -> Self:
        fen: str = str(styled)
        fen = fen + " w - - 0 1"
        board: chess.Board = chess.Board(fen)
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
        ans: list = list()
        for i in range(64):
            ans.append(self[Square(i).mirror()])
        return ans

    @classmethod
    def starting(cls: type, /) -> Self:
        return cls.byFENStyled("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR")
