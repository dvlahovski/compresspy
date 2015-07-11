from fileutils import CompressedFile


def open(filename, mode):
    return CompressedFile(filename, mode, LZW)

extension = ".lzw"


class LZW():
    def __init__(self):
        self.magic = b'\xba\xca'
        #TODO limit dict

    def compress(self, data):
        dictionary = dict([(bytes([i]), i) for i in range(256)])
        next_index = 256
        bit_width = 9
        codes = []
        key = bytes()
        packed_bytes = ""

        for i in data:
            current_byte = bytes([i])
            if key + current_byte in dictionary:
                key += current_byte
            else:
                bin_value = bin(dictionary[key])[2:]
                packed_bytes += '0' * (bit_width - len(bin_value)) + bin_value
                dictionary[key + current_byte] = next_index
                if len(bin(next_index)[2:]) > bit_width:
                    bit_width += 1
                next_index += 1
                key = current_byte

        bin_value = bin(dictionary[key])[2:]
        packed_bytes += '0' * (bit_width - len(bin_value)) + bin_value

        if len(packed_bytes) % 8 != 0:
            packed_bytes += '0' * (8 - len(packed_bytes) % 8)

        # pack everything into a bytearray taking 8 bits at a time
        output = bytearray()
        for i in range(0, len(packed_bytes), 8):
            output.append(int(packed_bytes[i:i+8], 2))

        return output

    def decompress(self, data):
        dictionary = dict([(i, bytes([i])) for i in range(256)])
        next_index = 256
        bit_width = 9
        position = 0
        result = bytearray()

        data_bin_str = ""
        for i in data:
            bin_i = bin(i)[2:]
            data_bin_str += '0' * (8 - len(bin_i)) + bin_i

        key = int(data_bin_str[position:position + bit_width], 2)
        sequence = dictionary[key]
        result.extend(sequence)
        position += bit_width

        while position + bit_width <= len(data_bin_str):
            key = int(data_bin_str[position:position + bit_width], 2)
            if key in dictionary:
                current = dictionary[key]
            elif key == next_index:
                current = sequence + bytes([sequence[0]])

            result.extend(current)
            dictionary[next_index] = sequence + bytes([current[0]])
            next_index += 1
            position += bit_width
            if len(bin(next_index)[2:]) > bit_width:
                bit_width += 1

            sequence = current

        return result
