'''
Write a program that calculates and prints the value according to the given formula:

Q = Square root of [(2 _ C _ D)/H]

Following are the fixed values of C and H:

C is 50. H is 30.

D is the variable whose values should be input to your program in a comma-separated sequence.For example
Let us assume the following comma separated input sequence is given to the program:

100,150,180

The output of the program should be:

18,22,24
'''

#solution
from math import sqrt

C,H=50,30

def calc(D):
    return sqrt( (2*C*D) / H)

D=[int(i) for i in input().split(',')] # suppose 100,150,180 is inputted 
D=[round(calc(i)) for i in D] #here calcule function works then round() is applied to floating values 
D=[str(i) for i in D] # values are converted into str because join works with strings 
D=",".join(D)
print(D)
