"""
Question
Please write a program to output a random number, which is divisible by 5 and 7, between 10 and 150 inclusive using random module and list comprehension.

Hints
Use random.choice() to a random element from a list.
"""

import random

numbers = [number for number in range(10, 151) if number % 35 == 0]

random_number = random.choice(numbers)

print(random_number)