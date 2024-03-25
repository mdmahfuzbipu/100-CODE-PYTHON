"""Question:
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

Hints:
Consider use class, function and comprehension."""

#solution

class My_gen:
    def by_seven(self,n):
        for i in range(0,int(n/7)+1):
            yield i*7


for i in range(My_gen.by_seven(int(input("Enter a number: ")))):
    print(i)