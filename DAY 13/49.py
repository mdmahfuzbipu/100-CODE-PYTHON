"""
Question
Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

Hints
To override a method in super class, we can define a method with the same name in the super class.
"""


class Shape:
    def area(self):
        return 0


class Square(Shape):
    def __init__(self, length=0):
        super().__init__()
        self.length = length
    
    
    def area(self):
        return self.length ** 2
    

sq = Square(5)
print(sq.area())

print(Square().area())