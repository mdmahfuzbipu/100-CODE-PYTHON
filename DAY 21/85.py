"""
Question
By using list comprehension, please write a program to print the list after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].

Hints
Use list comprehension to delete a bunch of element from a list.Use enumerate() to get (index, value) tuple.
"""

numbers = [12, 24, 35, 70, 88, 120, 155]

result = [number for  index, number in enumerate(numbers) if index not in (0,4,5)]

print(result)