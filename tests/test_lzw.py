import unittest
from compresspy import lzw
from random import randint


class TestLZW(unittest.TestCase):
    def setUp(self):
        self.compressor = lzw.LZW()
        # TOBEORNOTTOBEORTOBEORNOT

    def test(self):
        data = ""
        for i in range(10**6):
            data += chr(randint(97, 122))
        data_bytes = bytes(data, "utf-8")
        compressed_data = self.compressor.compress(data_bytes)
        # self.assertEqual(len(compressed_data), 16)
        # known_output = [84, 79, 66, 69, 79, 82, 78, 79, 84, 256, 258, 260,
        #                 265, 259, 261, 263]
        # self.assertEqual(compressed_data, known_output)
        # print(compressed_data)
        print(len(compressed_data))
        print((1 - len(compressed_data) / len(data))*100)

        self.assertEqual(data, self.compressor.decompress(compressed_data)
            .decode("utf-8"))

    def test_corner_case_in_LZW(self):
        data = "ASDASDASDASDASDASDASDASDASD"
        data_bytes = bytes(data, "utf-8")
        compressed_data = self.compressor.compress(data_bytes)
        self.assertEqual(data, self.compressor.decompress(compressed_data)
            .decode("utf-8"))

if __name__ == '__main__':
    unittest.main()
