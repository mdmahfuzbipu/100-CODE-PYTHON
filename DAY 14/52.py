"""
Question
Define a custom exception class which takes a string message as attribute.

Hints
To define a custom exception, we need to define a class inherited from Exception.
"""

class CustomEx(Exception):
    def __init__(self, msg):
        self.message = msg
        

num = int(input())


try:
    if num < 18:
        raise CustomEx("Age must be grater than 18")

except CustomEx as ce:
    print("The error raised: ", ce.message)