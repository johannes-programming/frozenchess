import unittest

from frozenchess.core.Piece import Piece
from frozenchess.core.Placement import Placement
from frozenchess.core.Square import Square


class TestPlacement(unittest.TestCase):
    def test_fen(self):
        self.assertEqual(Piece.byFENStyled("r"), Piece([0, "R"]))
        self.assertEqual(
            Piece.byFENStyled("R"), Piece(color=Piece.Color.WHITE, kind=Piece.Kind.ROOK)
        )
        self.assertEqual(
            Piece.byFENStyled("K"), Piece([Piece.Color.WHITE, Piece.Kind.KING])
        )
        self.assertEqual(
            Piece.byFENStyled("R"), Piece([Piece.Color.WHITE, Piece.Kind.ROOK])
        )
        self.assertEqual(
            Piece.byFENStyled("P"), Piece([Piece.Color.WHITE, Piece.Kind.PAWN])
        )

    def test_starting_position(self):
        placement = Placement.starting()
        self.assertEqual(placement[Square.A1], Piece.byFENStyled("R"))
        self.assertEqual(placement[Square.E1], Piece.byFENStyled("K"))
        self.assertEqual(placement[Square.D8], Piece.byFENStyled("q"))
        self.assertEqual(placement[Square.A3], None)

    def test_byFENStyled(self):
        fen = "8/8/8/8/8/8/PPP5/RNBQKBNR"
        placement = Placement.byFENStyled(fen)
        self.assertEqual(placement[Square.A1], Piece.byFENStyled("R"))
        self.assertEqual(placement[Square.C2], Piece.byFENStyled("P"))
        self.assertIsNone(placement[Square.E4])

    def test_fenStyled_output(self):
        input_fen = "8/8/8/8/8/8/PPP5/RNBQKBNR"
        placement = Placement.byFENStyled(input_fen)
        output_fen = placement.fenStyled()
        self.assertEqual(output_fen, input_fen)

    def test_mirror(self):
        placement = Placement.starting()
        mirrored = placement.mirror()
        self.assertEqual(
            mirrored[Square.A8], Piece([Piece.Color.WHITE, Piece.Kind.ROOK])
        )
        self.assertEqual(
            mirrored[Square.H7], Piece([Piece.Color.WHITE, Piece.Kind.PAWN])
        )
        self.assertEqual(
            mirrored[Square.E2], Piece([Piece.Color.BLACK, Piece.Kind.PAWN])
        )
        self.assertEqual(
            mirrored[Square.E1], Piece([Piece.Color.BLACK, Piece.Kind.KING])
        )

    def test_init_with_kwargs(self):
        placement = Placement(a1=Piece([1, "R"]), e8=Piece([0, "K"]))
        self.assertEqual(
            placement[Square.A1], Piece([Piece.Color.WHITE, Piece.Kind.ROOK])
        )
        self.assertEqual(
            placement[Square.E8], Piece([Piece.Color.BLACK, Piece.Kind.KING])
        )
        self.assertIsNone(placement[Square.D4])

    def test_invalid_other_too_long(self):
        with self.assertRaises(ValueError):
            Placement([None] * 65)  # Too many elements


if __name__ == "__main__":
    unittest.main()
