"""
Question
Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console.

Example:
If the following n is given as input to the program:

10

Then, the output of the program should be:

0,2,4,6,8,10

In case of input data being supplied to the question, it should be assumed to be a console input.

Hints
Use yield to produce the next value in generator.
"""

def generate_even(n):
    for i in range(0, n+1, 2):
        yield i
        

print(",".join( str(num) for num in generate_even(10)))