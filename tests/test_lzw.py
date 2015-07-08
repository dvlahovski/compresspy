import unittest
from compresspy import lzw

class TestLZW(unittest.TestCase):
    def setUp(self):
        self.compressor = lzw.LZW()

    def test(self):
        data = "TOBEORNOTTOBEORTOBEORNOT"
        data_bytes = bytes(data, "utf-8")
        compressed_data = self.compressor.compress(data_bytes)
        self.assertEqual(len(compressed_data), 16)
        known_output = [84, 79, 66, 69, 79, 82, 78, 79, 84, 256, 258, 260, 265, 259, 261, 263]
        self.assertEqual(compressed_data, known_output)


if __name__ == '__main__':
    unittest.main()
