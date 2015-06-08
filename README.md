# compresspy

## Description

Compresspy is a single-file compression/decompression tool, that supports the following algorithms:
* [LZW](http://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Welch "LZW")
* [Shannon-Fano coding](http://en.wikipedia.org/wiki/Shannon%E2%80%93Fano_coding "Shannon-Fano coding")
* [Huffman coding](http://en.wikipedia.org/wiki/Huffman_coding "Huffman coding")

## Usage

    $ python compress.py [options] file

### Options:
Should choose exactly one from "-c" and "-d"
* -c: Compress `file`. Should choose exactly one of the following options:
    * -l: Compress `file` using LZW
    * -s: Compress `file` using Shannon-Fano
    * -h: Compress `file` using Huffman
* -d: Decompress `file` 
* -v: verbose output

