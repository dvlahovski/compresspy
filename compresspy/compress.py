import lzw
# import shannon_fano_coding
# import huffman_coding

# TODO parse user options (argparse)

"""
Example usage:

read compressed file:
with lzw.open('/home/user/file.lzw', 'rb') as f:
    content = f.read()

create compressed file:
content = b"asdasdasd"
with lzw.open('/home/user/file.lzw', 'wb') as f:
    f.write(content)
"""
