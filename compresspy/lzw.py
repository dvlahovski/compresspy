from compresspy.fileutils import CompressedFile


def open(filename, mode):
    return CompressedFile(filename, mode, LZW)


class LZW():
    def __init__(self):
        self._magic = b'\012\034' # TODO specify the magic bytes
        self.max_dict_size = 1000 # TODO

    def compress(self, data):
        dictionary = dict([(bytes([i]), i) for i in range(256)])
        next_index = 256
        output = []
        key = bytes()
        for i in data:
            current_byte = bytes([i])
            if key + current_byte in dictionary:
                key += current_byte
            else:
                output.append(dictionary[key])
                dictionary[key + current_byte] = next_index
                next_index += 1
                key = current_byte

        output.append(dictionary[key])
        # print(data)
        # print(output)
        # import operator
        # sorted_x = sorted([i for i in dictionary.items() if i[1] >= 256 or i[1] >= 65 and i[1] <= 90] , key=operator.itemgetter(1))
        # for i in sorted_x:
        #     print(i)

        return output

    def decompress(self, data):
        pass
