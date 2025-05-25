import unittest

from frozenchess.core.File import File


class TestFile(unittest.TestCase):
    def test_enum_values(self):
        self.assertEqual(File.A.value, 0)
        self.assertEqual(File.H.value, 7)

    def test_native_uniqueness(self):
        # Ensure that mirrored positions match for symmetric pieces
        self.assertEqual(File.A.native(), File.H.native())
        self.assertEqual(File.B.native(), File.G.native())
        self.assertEqual(File.C.native(), File.F.native())


if __name__ == "__main__":
    unittest.main()
