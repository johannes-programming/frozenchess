import unittest

from frozenchess.core.Piece import Piece

Color = Piece.Color
Kind = Piece.Kind


class TestPiece(unittest.TestCase):

    def test_piece_initialization(self):
        p = Piece(color=Color.WHITE, kind=Kind.KNIGHT)
        self.assertEqual(p.color, Color.WHITE)
        self.assertEqual(p.kind, Kind.KNIGHT)

    def test_fen_parsing_white(self):
        p = Piece.byFENStyled("N")
        self.assertEqual(p.color, Color.WHITE)
        self.assertEqual(p.kind, Kind.KNIGHT)

    def test_fen_parsing_black(self):
        p = Piece.byFENStyled("n")
        self.assertEqual(p.color, Color.BLACK)
        self.assertEqual(p.kind, Kind.KNIGHT)

    def test_fen_styling(self):
        p = Piece(color=Color.BLACK, kind=Kind.QUEEN)
        self.assertEqual(p.fenStyled(), "q")

    def test_mirror(self):
        self.assertEqual(Color.WHITE, ~Color.BLACK)
        self.assertEqual(Color.WHITE, Color.BLACK.mirror())
        original = Piece(color=Color.WHITE, kind=Kind.BISHOP)
        mirrored = original.mirror()
        self.assertEqual(mirrored.kind, Kind.BISHOP)
        self.assertEqual(mirrored.color, Color.BLACK)
        self.assertNotEqual(original, mirrored)

    def test_uci_styled(self):
        self.assertEqual(Kind.KNIGHT.uciStyled(), "N")
        self.assertEqual(Kind.PAWN.uciStyled(), "")

    def test_uci_parse_error(self):
        with self.assertRaises(ValueError):
            Kind.byUCIStyled("K")  # disallowed

    def test_uci_parse_valid(self):
        self.assertEqual(Kind.byUCIStyled("N"), Kind.KNIGHT)

    def test_piece_equality(self):
        p1 = Piece(color=Color.WHITE, kind=Kind.ROOK)
        p2 = Piece(color=Color.WHITE, kind=Kind.ROOK)
        p3 = Piece(color=Color.BLACK, kind=Kind.ROOK)
        self.assertEqual(p1, p2)
        self.assertNotEqual(p1, p3)


if __name__ == "__main__":
    unittest.main()
