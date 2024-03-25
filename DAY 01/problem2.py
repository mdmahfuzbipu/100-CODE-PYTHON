'''
Write a program which can compute the factorial of a given numbers.The results should be printed in a comma-separated sequence on a single line.Suppose the following input is supplied to the program: 8
Then, the output should be:40320

'''

#solution 1 (lambda)

factorial = lambda n: 1 if n == 0 else n * factorial(n-1)
num=int(input())
print(factorial(num))

#solution 2 (while loop)
num = int(input())
fact = 1
i = 1

while i <= num:
    fact = fact * i 
    i = i + 1
print(fact)


#solution 3 ( for loop )
num = int(input())
result=1
for i in range (1 , num+1):
    result= num*i
print(result)
