import unittest

from frozenchess.core.File import File
from frozenchess.core.Piece import Kind


class TestFile(unittest.TestCase):
    def test_enum_values(self):
        self.assertEqual(File.A.value, 0)
        self.assertEqual(File.H.value, 7)

    def test_starting_uniqueness(self):
        # Ensure that mirrored positions match for symmetric pieces
        self.assertEqual(File.A.starting(), File.H.starting())
        self.assertEqual(File.B.starting(), File.G.starting())
        self.assertEqual(File.C.starting(), File.F.starting())


if __name__ == "__main__":
    unittest.main()
