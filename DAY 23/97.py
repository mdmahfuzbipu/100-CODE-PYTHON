"""
Question
You are given an integer, N. Your task is to print an alphabet rangoli of size N. (Rangoli is a form of Indian folk art based on creation of patterns.)

Different sizes of alphabet rangoli are shown below:

s
i
z
e
=
3
size=3

----c----

--c-b-c--

c-b-a-b-c

--c-b-c--

----c----

s
i
z
e
=
5
size=5

--------e--------

------e-d-e------

----e-d-c-d-e----

--e-d-c-b-c-d-e--

e-d-c-b-a-b-c-d-e

--e-d-c-b-c-d-e--

----e-d-c-d-e----

------e-d-e------

--------e--------

Hints
First print the half of the Rangoli in the given way and save each line in a list. Then print the list in reverse order to get the rest.
"""


import string


def print_rangoli(n):
    alphabet = string.ascii_lowercase
    lines = []

    for i in range(n):
        left = alphabet[n - 1 : i : -1]  
        center = alphabet[i:n]  
        row_letters = left + center
        row = "-".join(row_letters)
        lines.append(row.center(4 * n - 3, "-"))

    for line in lines[::-1]:
        print(line)
    for line in lines[1:]:
        print(line)


print_rangoli(5)


print_rangoli(5)
