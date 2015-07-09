import unittest
from compresspy import lzw
from random import randint


class TestLZW(unittest.TestCase):
    def setUp(self):
        self.compressor = lzw.LZW()

    def compress(self, data):
        data_bytes = bytes(data, "utf-8")
        return self.compressor.compress(data_bytes)

    def decompress(self, data):
        return self.compressor.decompress(data).decode("utf-8")

    def compare(self, data):
        compressed_data = self.compress(data)
        decompressed_data = self.decompress(compressed_data)
        self.assertEqual(data, decompressed_data)

    def test_wikipedia_example(self):
        data = "TOBEORNOTTOBEORTOBEORNOT"
        self.compare(data)

    def test_random_lowercase_letters(self):
        data = ""
        for i in range(10**4):
            data += chr(randint(97, 122))
        self.compare(data)

    def test_corner_case_in_LZW(self):
        data = "ASDASDASDASDASDASDASDASDASD"
        self.compare(data)

if __name__ == '__main__':
    unittest.main()
