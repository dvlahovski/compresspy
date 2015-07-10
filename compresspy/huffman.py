from fileutils import CompressedFile
from collections import Counter
from heapq import heapify, heappush, heappop
import queue
from bitstring import BitStream, ReadError


def open(filename, mode):
    return CompressedFile(filename, mode, Huffman)


class HuffmanNode():
    def __init__(self, left=None, right=None, value=None, weight=None):
        self.left = left
        self.right = right
        self.value = value
        self.code = ""
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight

    def leaf(self):
        return self.value is not None

    def assign_codes(self, prefix=""):
        if self.leaf():
            self.code = prefix
            return {self.value: self.code}

        left_codes = self.left.assign_codes(prefix + '1')
        right_codes = self.right.assign_codes(prefix + '0')
        left_codes.update(right_codes)
        return left_codes

    def serialize(self):
        bitstream = BitStream()
        if self.leaf():
            bitstream.append('bin=1')
            bitstream.append("{0:#0{1}x}".format(self.value, 4))
        else:
            bitstream.append('bin=0')
            bitstream += self.left.serialize() + self.right.serialize()

        return bitstream

    def deserialize(self, bitstream):
        if bitstream.read(1).bin == '1':
            self.value = bitstream.read(8).uint
        else:
            self.value = None
            self.left = HuffmanNode()
            self.left.deserialize(bitstream)
            self.right = HuffmanNode()
            self.right.deserialize(bitstream)


class Huffman():
    def __init__(self):
        self._magic = b'\xba\xda'

    def compress(self, data):
        weight = Counter(data)
        priority_queue = [HuffmanNode(value=byte, weight=weight[byte])
                          for byte in weight]
        heapify(priority_queue)

        while len(priority_queue) > 1:
            left = heappop(priority_queue)
            right = heappop(priority_queue)
            node = HuffmanNode(left, right, weight=left.weight + right.weight)
            heappush(priority_queue, node)

        root = heappop(priority_queue)
        dictionary = root.assign_codes()
        """
        we need to add the tree to the compressed data, so that the
        decompressor can rebuild it in order do to it's work
        """
        tree = root.serialize()
        result = BitStream()
        tree_len_bits = len(bin(len(tree))[2:])
        if tree_len_bits > 16:
            raise ValueError("Huffman tree len is max 10*255-1 bit")

        # this converts len(tree) to hex with zero front pad to two bytes
        result.append("{0:#0{1}x}".format(len(tree), 6))
        result += tree

        for byte in data:
            result.append('bin=' + dictionary[byte])

        pad = 0
        if len(result) % 8 != 0:
            pad = 8 - len(result) % 8
            result.append('bin=' + '0' * pad)

        """
        the compressed data layout is as follows:
        * 1B - number of pad bits (for byte align)
        * 2B- Huffman tree length (which btw = 10*num_of_chars_in_the_tree -1)
        * the Huffman tree itself (not byte aligned)
        * the encoded data paded with 0-7 bits at the end
        """
        result = BitStream("{0:#0{1}x}".format(pad, 4)) + result
        return bytearray(result.bytes)

    def decompress(self, data):
        bitstream = BitStream(data)
        pad = bitstream.read(8).int
        # remove pad bits
        if pad > 0:
            bitstream = bitstream[:-pad]
            bitstream.read(8)  # false read 1 B to move read pointer

        tree_len = bitstream.read(16).int
        tree_serial = bitstream.read(tree_len)
        tree = HuffmanNode()
        tree.deserialize(tree_serial)
        dictionary = tree.assign_codes()
        dictionary = {v: k for k, v in dictionary.items()}  # reverse dict
        result = bytearray()
        sequence = ""

        while True:
            try:
                bit = bitstream.read(1)
            except ReadError:
                break

            if bit:
                sequence += '1'
            else:
                sequence += '0'

            if sequence in dictionary:
                result.append(dictionary[sequence])
                sequence = ""

        return result
