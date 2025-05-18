import unittest

from frozenchess.core.BitBoard import BitBoard


class TestBitBoard(unittest.TestCase):

    def test_individual_squares(self):
        self.assertEqual(BitBoard.A1.value, 1)
        self.assertEqual(BitBoard.H1.value, 128)
        self.assertEqual(BitBoard.A8.value, 72057594037927936)
        self.assertEqual(BitBoard.H8.value, 9223372036854775808)

    def test_combination_of_squares(self):
        combo = BitBoard.A1 | BitBoard.B1
        self.assertTrue(combo & BitBoard.A1)
        self.assertTrue(combo & BitBoard.B1)
        self.assertFalse(combo & BitBoard.C1)

    def test_all_squares_unique(self):
        seen = set()
        for square in BitBoard:
            self.assertNotIn(square.value, seen, f"Duplicate value: {square.name}")
            seen.add(square.value)

    def test_combined_flag_contains_all_parts(self):
        combined = BitBoard.C1 | BitBoard.D2 | BitBoard.E3
        self.assertIn(BitBoard.C1, combined)
        self.assertIn(BitBoard.D2, combined)
        self.assertIn(BitBoard.E3, combined)
        self.assertNotIn(BitBoard.F4, combined)


if __name__ == "__main__":
    unittest.main()
