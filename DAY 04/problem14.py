'''
Question:
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

Suppose the following input is supplied to the program:

Hello world!

Then, the output should be:

UPPER CASE 1

LOWER CASE 9

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''
#solution 1

word=input()
upper,lower=0,0

for i in word:
    if "a" <= i and i <= "z":
        lower+=1
    if "A" <= i and i <= "Z":
        upper+=1

print("Upper case {0}\nLower case {1}".format(upper,lower))

#solution 2

word=input()
upper=sum(1 for i in word if i.isupper()) #generator expression
lower=sum(1 for i in word if i.islower()) #generates 1s for each character i in word that is lowercase

print("upper letter: "+str(upper)+"\nlower letter: "+str(lower))