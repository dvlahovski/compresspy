from fileutils import CompressedFile


def open(filename, mode):
    return CompressedFile(filename, mode, LZW)


class LZW():
    def __init__():
        self._magic = b'\012\034' # TODO specify the magic bytes

    def compress(data):
        pass

    def decompress(data):
        pass
