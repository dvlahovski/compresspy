from fileutils import CompressedFile


def open(filename, mode):
    return CompressedFile(filename, mode, Huffman)


class Huffman():
    def __init__(self):
        self._magic = b'\xba\xda'  # TODO specify the magic bytes

    def compress(self, data):
        pass

    def decompress(self, data):
        pass
