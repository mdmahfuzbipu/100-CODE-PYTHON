"""
Question
Write a program to read an ASCII string and to convert it to a unicode string encoded by utf-8.

Hints
Use unicode()/encode() function to convert.
"""

s = input()
encoded = s.encode('utf-8')
print(encoded)