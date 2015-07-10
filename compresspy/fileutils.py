import io
import struct


class CompressedFile(io.BufferedIOBase):
    """
    The CompressedFile class simulates a file object
    """
    def __init__(self, filename, mode, compressor):
        self._filename = filename
        self._mode = mode
        self._compressor = compressor()
        self._fileobj = open(filename, mode)  # XXX mode rb or wb
        # self._chunksize = 1024

    def write_header(self):
        self._fileobj.write(self._compressor._magic)
        # if len(bin(self._chunksize)[2:]) > 8*4:
        #     raise ValueError("chunksize must be at most 4 bytes")
        #
        # self.fileobj.write(struct.pack("I", self._chunksize))

    def read_header(self):
        magic = self._fileobj.read(2)
        if magic != self._compressor._magic:
            raise TypeError("not a {} file"
                            .format(self._compressor.__class__.__name__))

    """
    Use self._compressor.decompress()
    """
    def read(self, size=-1):
        self.read_header()
        data = self._fileobj.read()
        return self._compressor.decompress(data)

    """
    Use self._compressor.compress()
    """
    def write(self, data):
        self.write_header()
        self._fileobj.write(self._compressor.compress(data))
