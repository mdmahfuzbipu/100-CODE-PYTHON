"""
Question
You are given a string S and width W.
Your task is to wrap the string into a paragraph of width.

If the following string is given as input to the program:

ABCDEFGHIJKLIMNOQRSTUVWXYZ
4

Then, the output of the program should be:

ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ

Hints
Use wrap function of textwrap module
"""

# s="ABCDEFGHIJKLIMNOQRSTUVWXYZ"
# w=4

# for i in range(0,len(s),w):
#     print(s[i:i+w])


import textwrap

print("\n".join(textwrap.wrap(input(), int(input()))))