"""
Question:
Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).

Hints:
Use map() to generate a list. Use lambda to define anonymous functions.
"""

def square(x):
    return x*x

numbers = list(map(square, range(1,21)))

print(numbers)
