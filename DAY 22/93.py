"""
Question
Please write a program which prints all permutations of [1,2,3]

Hints
Use itertools.permutations() to get permutations of list.
"""

import itertools

numbers = [1,2,3]

perms = itertools.permutations(numbers)

for p in perms:
    print(p)