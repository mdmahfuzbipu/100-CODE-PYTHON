"""
Question
By using list comprehension, please write a program to print the list after removing numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].

Hints
Use list comprehension to delete a bunch of element from a list.
"""

numbers = [12, 24, 35, 70, 88, 120, 155]

filtered_numbers = [num for num in numbers if num % 35 != 0]

print(filtered_numbers)