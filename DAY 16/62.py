"""
Question
The Fibonacci Sequence is computed based on the following formula:

> $f(n)=0$ if n=0

> $f(n)=1$ if n=1

> $f(n)=f(n-1)+f(n-2)$ if n>1

Please write a program to compute the value of f(n) with a given n input by console.

Example:
If the following n is given as input to the program:

7

Then, the output of the program should be:

0,1,1,2,3,5,8,13

In case of input data being supplied to the question, it should be assumed to be a console input.

Hints
We can define recursive function in Python.
Use list comprehension to generate a list from an existing list.
Use string.join() to join a list of strings.
"""

def f(n):
    if n < 2:
        fibo[n] = n
        return n

    fibo[n] = f(n-1) + f(n-2)
    return fibo[n]

number = int(input())
fibo = [0] * (number + 1)

f(number)

    
print(",".join(str(i) for i in fibo))