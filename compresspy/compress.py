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
#TODO add "No compression - file unchanged"

# with open('/home/dvlahovski/Desktop/test/1.mp3', 'rb') as f:
#     content = f.read()
#
# with lzw.open('/home/dvlahovski/Desktop/test/1.lzw', 'wb') as f:
#     f.write(content)
#
# with lzw.open('/home/dvlahovski/Desktop/test/1.lzw', 'rb') as f:
#     content = f.read()
#
# with open('/home/dvlahovski/Desktop/test/2.mp3', 'wb') as f:
#     f.write(content)
