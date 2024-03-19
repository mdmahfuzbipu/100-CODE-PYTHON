"""
Question:
Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:

D 100
W 200
D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:

D 300
D 300
W 200
D 100
Then, the output should be:

500
"""

total=0 

while True:
    s=input().split() 
    if not s: # if enter is pressed two times the loop will exit and show the result 
        break
    cm,nm=map(str,s) # two inputs are distributed in cm and nm in string data type

    if cm == "D":
        total+=int(nm)
    elif cm == "W":
        total-=int(nm)
print(total)