import unittest
from compresspy import huffman
from heapq import heapify, heappop, heappush
from collections import Counter
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

    def generate_tree(self, data):
        weight = Counter(data)
        priority_queue = [huffman.HuffmanNode(value=byte, weight=weight[byte])
                          for byte in weight]
        heapify(priority_queue)

        while len(priority_queue) > 1:
            left = heappop(priority_queue)
            right = heappop(priority_queue)
            node = huffman.HuffmanNode(left, right,
                                       weight=left.weight + right.weight)
            heappush(priority_queue, node)

        root = heappop(priority_queue)
        return root

    def test(self):
        data = "this is an example of a huffman tree which is a good example\
        if it has a lot of text in it I truly hope"
        self.compare(data)

    def test_random(self):
        data = ""
        for i in range(10**3):
            data += chr(randint(97, 122))
        self.compare(data)

    def test_serialize(self):
        data = b"this is an example of a huffman tree"
        tree = self.generate_tree(data)
        serial = tree.serialize()
        new_tree = huffman.HuffmanNode()
        new_tree.deserialize(serial)
        self.assertEqual(tree.assign_codes(), new_tree.assign_codes())

    def test_is_prefix_tree(self):
        pass

if __name__ == '__main__':
    unittest.main()
