import argparse
import os
from time import time
import lzw
import huffman


def init_args():
    parser = argparse.ArgumentParser(description='compresspy - \
                                     single file compression tool')
    parser.add_argument('-c', default=False, action='store_true',
                        help='Compress file')
    parser.add_argument('-l', default=False, action='store_true',
                        help='LZW')
    parser.add_argument('-u', default=False, action='store_true',
                        help='Huffman coding')
    parser.add_argument('-d', default=False, action='store_true',
                        help='Decompress file')
    parser.add_argument('-v', default=False, action='store_true',
                        help='Verbose')
    parser.add_argument('filepath', help='Filepath')

    args = parser.parse_args()
    return args


def validate_args(args):
    if args.c and args.d:
        print("Choose exactly one of -c and -d")
        exit(-1)

    if args.c and not args.l and not args.u:
        print("Choose compression algo (either -l or -u)")
        exit(-1)

    if args.c and args.l and args.u:
        print("Choose exactly one of -l and -u")
        exit(-1)


def get_name_of_compressed(filename, ext):
    dest_dir = os.path.dirname(filename)
    name = os.path.basename(filename)
    dot = name.find('.')
    name = name[:dot]
    return dest_dir + os.path.sep + name + ext


def main():
    args = init_args()
    validate_args(args)

    compressor = None
    if args.c:  # compression
        if args.l:
            compressor = lzw
        elif args.u:
            compressor = huffman

        dest_name = ""
        content = None
        with open(args.filepath, 'rb') as f:
            content = f.read()
            dest_name = get_name_of_compressed(f.name, compressor.extension)
        start = time()
        compressed_size = None
        with compressor.open(dest_name, 'wb') as f:
            compressed_size = f.write(content)
            if compressed_size == -1:
                print("Can't compress - leaving unchanged")
                exit(-1)
        end = time()
        savings = (1 - (compressed_size / len(content)))*100

    elif args.d:  # decompression
        with open(args.filepath, 'rb') as f:
            magic = f.read(2)
            if magic == lzw.LZW().magic:
                compressor = lzw
            elif magic == huffman.Huffman().magic:
                compressor = huffman
            else:
                raise ValueError("wrong magic byte\
                                  - neither LZW nor Huffman file")
        dest_name = ""
        content = None
        start = time()
        with compressor.open(args.filepath, 'rb') as f:
            content = f.read()
            dest_name = get_name_of_compressed(f.name, ".decompressed")
        end = time()

        with open(dest_name, 'wb') as f:
            f.write(content)

    if args.v:
        print("elapsed time: {0:.2f} s".format(end-start))
        if args.c:
            print("space savings: {0:.2f} %".format(savings))

if __name__ == '__main__':
    main()
