"""
Question
Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area.

Hints
Use def methodName(self) to define a method.
"""


class Rectangle:
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def area(self):
        return self.length * self.width
    

rec = Rectangle(5,7)
print(rec.area())
