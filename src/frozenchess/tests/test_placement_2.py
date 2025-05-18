import unittest

from frozenchess.core.Piece import Color, Kind, Piece
from frozenchess.core.Placement import Placement
from frozenchess.core.Square import Square


class TestPlacement(unittest.TestCase):
    def test_starting_position(self):
        placement = Placement.starting()
        self.assertEqual(placement[Square.A1], Piece(color=Color.WHITE, kind=Kind.ROOK))
        self.assertEqual(placement[Square.E1], Piece(color=Color.WHITE, kind=Kind.KING))
        self.assertEqual(placement[Square.A2], Piece(color=Color.WHITE, kind=Kind.PAWN))
        self.assertEqual(placement[Square.A7], Piece(color=Color.BLACK, kind=Kind.PAWN))
        self.assertEqual(placement[Square.E8], Piece(color=Color.BLACK, kind=Kind.KING))
        self.assertIsNone(placement[Square.D4])

    def test_fen_round_trip(self):
        fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
        placement = Placement.byFENStyled(fen)
        self.assertEqual(placement.fenStyled(), fen)

    def test_partial_fen(self):
        fen = "8/8/8/8/3k4/8/8/8"
        placement = Placement.byFENStyled(fen)
        self.assertEqual(placement[Square.D4], Piece(color=Color.BLACK, kind=Kind.KING))
        self.assertIsNone(placement[Square.E4])
        self.assertEqual(placement.fenStyled(), fen)

    def test_mirror(self):
        original = Placement.starting()
        mirrored = original.mirror()
        self.assertEqual(mirrored[Square.A8], original[Square.A1])
        self.assertEqual(mirrored[Square.H7], original[Square.H2])
        self.assertIsNone(mirrored[Square.D4])

    def test_from_kwargs(self):
        placement = Placement(
            a1=Piece(color=Color.WHITE, kind=Kind.ROOK),
            d5=Piece(color=Color.BLACK, kind=Kind.QUEEN),
        )
        self.assertEqual(placement[Square.A1], Piece(color=Color.WHITE, kind=Kind.ROOK))
        self.assertEqual(
            placement[Square.D5], Piece(color=Color.BLACK, kind=Kind.QUEEN)
        )
        self.assertIsNone(placement[Square.E4])

    def test_invalid_init_too_long(self):
        long_list = [None] * 65
        with self.assertRaises(ValueError):
            Placement(long_list)

    def test_piece_is_cast_to_proper_type(self):
        raw_data = [
            Piece(color=Color.WHITE, kind=Kind.KNIGHT) if i == Square.B1 else None
            for i in range(64)
        ]
        placement = Placement(raw_data)
        self.assertIsInstance(placement[Square.B1], Piece)
        self.assertEqual(placement[Square.B1].kind, Kind.KNIGHT)
        self.assertIsNone(placement[Square.C1])


if __name__ == "__main__":
    unittest.main()
