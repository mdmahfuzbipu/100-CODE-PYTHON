'''
Question:
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.

Suppose the following input is supplied to the program:

Hello world

Practice makes perfect

Then, the output should be:

HELLO WORLD

PRACTICE MAKES PERFECT
'''

#solution 9

lines=[]

while True:
    line=input("Enter lines : ")
    if line:
        lines.append(line.upper())
    else:
        break

for line in lines:
    print(line)

#solution
    
def user_input():
    while True:
        x=input("Enter lines: ")
        if x:
            yield x
        else: 
            break
for line in map(str.upper,user_input()):
    print(line)


