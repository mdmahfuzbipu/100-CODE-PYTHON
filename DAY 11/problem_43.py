"""
Question:
Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).

Hints:
Use filter() to filter elements of a list.Use lambda to define anonymous functions.
"""


even_numbers = list(filter(lambda x : x % 2 == 0, [i+1 for i in range(20)]))

print(even_numbers)

# solutin 2

numbers = list(range(1,21))
EvenNumber=list(filter(lambda x : x % 2 == 0, numbers))

print(EvenNumber)