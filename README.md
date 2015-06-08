# compresspy

## Description

Compresspy is a single-file compression tool, that supports the following compression algos:
* [LZW](http://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Welch "LZW")
* [Shannon-Fano coding](http://en.wikipedia.org/wiki/Shannon%E2%80%93Fano_coding "Shannon-Fano coding")
* [Huffman coding](http://en.wikipedia.org/wiki/Huffman_coding "Huffman coding")

## Usage

    $ python compress.py -l|-s|-h [other_options] file

### Options:
* -l: Compress `file` using LZW
* -s: Compress `file` using Shannon-Fano
* -h: Compress `file` using Huffman
* -v: verbose output

