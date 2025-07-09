"""
Question
By using list comprehension, please write a program to print the list after removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].

Hints
Use list comprehension to delete a bunch of element from a list.
Use enumerate() to get (index, value) tuple.
"""

numbers = [12, 24, 35, 70, 88, 120, 155]

remove = [0, 2, 4, 6]

result = [value for index,value in enumerate(numbers) if index not in remove]

print(result)