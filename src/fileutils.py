class CompressedFile(io.BufferedIOBase):
    """
    The CompressedFile class simulates a file object
    """
    def __init__(self, filename, mode, compressor):
        self._filename = filename
        self._mode = mode
        self._compressor = compressor()

    """
    Use self._compressor.decompress()
    """
    def read():
        pass

    """
    Use self._compressor.compress()
    """
    def write():
        pass
