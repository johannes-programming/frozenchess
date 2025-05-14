import unittest

from frozenchess.core.Piece import Color, Kind, Piece
from frozenchess.core.Placement import Placement
from frozenchess.core.Square import Square


class TestPlacement(unittest.TestCase):
    def test_starting_position(self):
        placement = Placement.starting()
        self.assertEqual(placement[Square.A1], Piece(Color.WHITE, Kind.ROOK))
        self.assertEqual(placement[Square.E1], Piece(Color.WHITE, Kind.KING))
        self.assertEqual(placement[Square.D8], Piece(Color.BLACK, Kind.QUEEN))
        self.assertEqual(placement[Square.A3], None)

    def test_byFENStyled(self):
        fen = "8/8/8/8/8/8/PPP5/RNBQKBNR"
        placement = Placement.byFENStyled(fen)
        self.assertEqual(placement[Square.A1], Piece(Color.WHITE, Kind.ROOK))
        self.assertEqual(placement[Square.C2], Piece(Color.WHITE, Kind.PAWN))
        self.assertIsNone(placement[Square.E4])

    def test_fenStyled_output(self):
        input_fen = "8/8/8/8/8/8/PPP5/RNBQKBNR"
        placement = Placement.byFENStyled(input_fen)
        output_fen = placement.fenStyled()
        self.assertEqual(output_fen, input_fen)

    def test_mirror(self):
        placement = Placement.starting()
        mirrored = placement.mirror()
        self.assertEqual(mirrored[Square.A8], Piece(Color.WHITE, Kind.ROOK))
        self.assertEqual(mirrored[Square.H7], Piece(Color.WHITE, Kind.PAWN))
        self.assertEqual(mirrored[Square.E2], Piece(Color.BLACK, Kind.PAWN))
        self.assertEqual(mirrored[Square.E1], Piece(Color.BLACK, Kind.KING))

    def test_init_with_kwargs(self):
        placement = Placement(
            A1=Piece(Color.WHITE, Kind.ROOK), E8=Piece(Color.BLACK, Kind.KING)
        )
        self.assertEqual(placement[Square.A1], Piece(Color.WHITE, Kind.ROOK))
        self.assertEqual(placement[Square.E8], Piece(Color.BLACK, Kind.KING))
        self.assertIsNone(placement[Square.D4])

    def test_invalid_other_too_long(self):
        with self.assertRaises(ValueError):
            Placement([None] * 65)  # Too many elements


if __name__ == "__main__":
    unittest.main()
