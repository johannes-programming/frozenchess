import unittest

from frozenchess.core.File import File
from frozenchess.core.Piece import Piece
from frozenchess.core.Square import Square


class TestSquare(unittest.TestCase):

    def test_uci_parsing(self):
        self.assertEqual(Square.byUCIStyled("a1"), Square.A1)
        self.assertEqual(Square.byUCIStyled("H8"), Square.H8)
        with self.assertRaises(ValueError):
            Square.byUCIStyled("z9")

    def test_uci_styling(self):
        self.assertEqual(Square.A1.uciStyled(), "a1")
        self.assertEqual(Square.H8.uciStyled(), "h8")

    def test_color(self):
        self.assertEqual(Square.A1.color(), Square.Color.DARK)
        self.assertEqual(Square.B1.color(), Square.Color.LIGHT)
        self.assertEqual(Square.C1.color(), Square.Color.DARK)
        self.assertEqual(Square.D1.color(), Square.Color.LIGHT)

    def test_file_and_rank(self):
        self.assertEqual(Square.A1.file(), File.A)
        self.assertEqual(Square.A1.rank(), 1)
        self.assertEqual(Square.H8.file(), File.H)
        self.assertEqual(Square.H8.rank(), 8)

    def test_mirror(self):
        self.assertEqual(Square.A1.mirror(), Square.A8)
        self.assertEqual(Square.E2.mirror(), Square.E7)
        self.assertEqual(Square.D4.mirror(), Square.D5)

    def test_starting_white_back_rank(self):
        self.assertEqual(
            Square.A1.starting(), Piece(color=Piece.Color.WHITE, kind=Piece.Kind.ROOK)
        )
        self.assertEqual(
            Square.E1.starting(), Piece(color=Piece.Color.WHITE, kind=Piece.Kind.KING)
        )

    def test_starting_white_pawns(self):
        self.assertEqual(
            Square.A2.starting(), Piece(color=Piece.Color.WHITE, kind=Piece.Kind.PAWN)
        )

    def test_starting_black_pawns(self):
        self.assertEqual(
            Square.H7.starting(), Piece(color=Piece.Color.BLACK, kind=Piece.Kind.PAWN)
        )

    def test_starting_black_back_rank(self):
        self.assertEqual(
            Square.H8.starting(), Piece(color=Piece.Color.BLACK, kind=Piece.Kind.ROOK)
        )
        self.assertEqual(
            Square.D8.starting(), Piece(color=Piece.Color.BLACK, kind=Piece.Kind.QUEEN)
        )

    def test_non_starting_squares_have_none(self):
        self.assertIsNone(Square.A3.starting())
        self.assertIsNone(Square.E4.starting())

    def test_all_squares_unique(self):
        squares = list(Square)
        self.assertEqual(len(squares), 64)
        self.assertEqual(len(set(s.value for s in squares)), 64)


if __name__ == "__main__":
    unittest.main()
