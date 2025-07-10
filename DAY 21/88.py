"""
Question
With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all duplicate values with original order reserved.

Hints
Use set() to store a number of values without duplicate.
"""
numbers = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]

seen = set()

result = [number for number in numbers if number not in seen and not seen.add(number)]

print(result)
