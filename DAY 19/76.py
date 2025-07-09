"""
Question
Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".

Hints
Use zlib.compress() and zlib.decompress() to compress and decompress a string.
"""

import zlib

txt = "hello world!hello world!hello world!hello world!"

txt_bytes = txt.encode('utf-8')

compressed_txt = zlib.compress(txt_bytes)

print(compressed_txt)


decompressed = zlib.decompress(compressed_txt)

original_txt = decompressed.decode('utf-8')

print(original_txt)