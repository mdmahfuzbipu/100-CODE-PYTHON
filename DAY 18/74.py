"""
Question
Please write a program to randomly generate a list with 5 numbers, which are divisible by 5 and 7 , between 1 and 1000 inclusive.

Hints
Use random.sample() to generate a list of random values.
"""

import random

numbers = [number for number in range(1, 1001) if number % 35 == 0]

five_numbers = random.sample(numbers, 5)

print(five_numbers)