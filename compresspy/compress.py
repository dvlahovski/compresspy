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

with open('/home/dvlahovski/Desktop/test/lev.txt', 'rb') as f:
    content = f.read()

with lzw.open('/home/dvlahovski/Desktop/test/1.lzw', 'wb') as f:
    f.write(content)

with lzw.open('/home/dvlahovski/Desktop/test/1.lzw', 'rb') as f:
    content = f.read()

with open('/home/dvlahovski/Desktop/test/lev2.txt', 'wb') as f:
    f.write(content)
