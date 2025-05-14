import unittest

from frozenchess.core.BitBoard import BitBoard


class TestBitBoard(unittest.TestCase):
    def test_single_square_values(self):
        # Spot-check a few squares for correct bit values
        self.assertEqual(BitBoard.A1.value, 1)
        self.assertEqual(BitBoard.B1.value, 2)
        self.assertEqual(BitBoard.H8.value, 9223372036854775808)

    def test_bitwise_or(self):
        board = BitBoard.A1 | BitBoard.B2
        self.assertTrue(BitBoard.A1 in board)
        self.assertTrue(BitBoard.B2 in board)
        self.assertFalse(BitBoard.C3 in board)

    def test_bitwise_and(self):
        board = BitBoard.A1 | BitBoard.B1
        self.assertEqual(board & BitBoard.A1, BitBoard.A1)
        self.assertEqual(board & BitBoard.C1, BitBoard(0))

    def test_flag_combination_membership(self):
        board = BitBoard.D4 | BitBoard.E4
        self.assertIn(BitBoard.D4, board)
        self.assertIn(BitBoard.E4, board)
        self.assertNotIn(BitBoard.F4, board)

    def test_mod_method(self):
        self.assertEqual(BitBoard._mod(), 2**64)

    def test_enum_completeness(self):
        # Ensure 64 distinct values for 64 squares
        all_values = set(member.value for member in BitBoard)
        self.assertEqual(len(all_values), 64)
        self.assertEqual(
            sum(1 for v in all_values if v & (v - 1) == 0), 64
        )  # all are powers of two


if __name__ == "__main__":
    unittest.main()
