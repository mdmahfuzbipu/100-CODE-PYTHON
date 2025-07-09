"""
Question
Please write a program to output a random even number between 0 and 10 inclusive using random module and list comprehension.

Hints
Use random.choice() to a random element from a list.
"""

import random

numbers = [number for number in range(0,11,2) if number % 2 == 0]

random_number = random.choice(numbers)

print(random_number)