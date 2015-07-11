import io
import struct


class CompressedFile(io.BufferedIOBase):
    """
    The CompressedFile class simulates a file object
    """
    def __init__(self, filename, mode, compressor):
        self.filename = filename
        self.mode = mode
        self.compressor = compressor()
        if mode not in ['rb', 'wb']:
            raise ValueError('only rb and wb modes supported')
        self.fileobj = open(filename, mode)
        self.name = self.fileobj.name

    def write_header(self):
        self.fileobj.write(self.compressor.magic)

    def read_header(self):
        magic = self.fileobj.read(2)
        if magic != self.compressor.magic:
            raise TypeError("not a {} file"
                            .format(self.compressor.__class__.__name__))

    def read(self, size=-1):
        self.read_header()
        data = self.fileobj.read()
        return self.compressor.decompress(data)

    def write(self, data):
        compressed = self.compressor.compress(data)
        if len(compressed) > len(data):
            return -1
        self.write_header()
        self.fileobj.write(compressed)
        return len(compressed)
