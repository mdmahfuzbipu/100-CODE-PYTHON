"""
Question
Please write a program which count and print the numbers of each character in a string input by console.

Example:
If the following string is given as input to the program:

abcdefgabc
Then, the output of the program should be:

a,2
c,2
b,2
e,1
d,1
g,1
f,1
"""

txt = "abcdefgabc"

char_cnt = {}

for i in txt:
    char_cnt[i] = char_cnt.get(i,0) + 1

for char in txt:
    if char in char_cnt:
        print(char,char_cnt[char])
        del char_cnt[char]
