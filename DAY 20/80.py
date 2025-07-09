"""
Question
Please write a program to print the list after removing even numbers in [5,6,77,45,22,12,24].

Hints
Use list comprehension to delete a bunch of element from a list.
"""


numbers = [5, 6, 77, 45, 22, 12, 24]

odd_numbers = [number for number in numbers if number % 2 != 0]

print(odd_numbers)