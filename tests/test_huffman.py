import unittest
from compresspy import huffman
from random import randint


class TestHuffman(unittest.TestCase):
    def setUp(self):
        self.compressor = huffman.Huffman()

    def compress(self, data):
        data_bytes = bytes(data, "utf-8")
        return self.compressor.compress(data_bytes)

    def decompress(self, data):
        return self.compressor.decompress(data).decode("utf-8")

    def compare(self, data):
        compressed_data = self.compress(data)
        decompressed_data = self.decompress(compressed_data)
        self.assertEqual(data, decompressed_data)

    # def test(self):
    #     data = "this is an example of a huffman tree"
    #     self.compare(data)

    def test_random(self):
        data = bytearray()
        for i in range(63):
            data.append(randint(0, 255))
        # print(len(data))
        compressed = self.compressor.compress(data)
        decompressed = self.compressor.decompress(compressed)
        self.assertEqual(data, decompressed)

    def test_serialize(self):
        pass

    def test_is_prefix_tree(self):
        pass

if __name__ == '__main__':
    unittest.main()
