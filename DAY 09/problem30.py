"""
Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print all strings line by line.
"""

#solution

maximum_str= lambda x,y: print(max((x,y),key=len)) if len(x) != len(y) else x + "\n" + y

maximum_str("mina","re")
