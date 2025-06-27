"""
Question
Write a function to compute 5/0 and use try/except to catch the exceptions.

Hints
Use try/except to catch exceptions.
"""


def divide(n, m):
    return n / m


try:
    n = int(input())
    m = int(input())
    divide(n, m)
except ZeroDivisionError as Ze:
    print(Ze, "not allowed")
except Exception as E:
    print("An Error occured ", E)
