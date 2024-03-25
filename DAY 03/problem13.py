'''
Question:
Write a program that accepts a sentence and calculate the number of letters and digits.

Suppose the following input is supplied to the program:

hello world! 123

Then, the output should be:

LETTERS 10

DIGITS 3
'''

#solution 

word=input()
letter,digit=0,0

for i in word:
    if ("a" <= i and "z" <= i) or ("A" <=i and "Z"<=i):
        letter+=1
    if "0"<= i and "9"<=i :
        digit+=1
print("Letters {}\nDigits {}".format(letter,digit))

#solution 2

word = input()
letter, digit = 0, 0

for i in word:
    if i.isalpha():  # returns True if alphabet
        letter += 1
    elif i.isnumeric():  # returns True if numeric
        digit += 1
print(
    f"LETTERS {letter}\nDigits {digit}"
)  # two different types of formating method is shown in both solution