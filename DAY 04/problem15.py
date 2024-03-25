'''
Question:
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.

Suppose the following input is supplied to the program:

9

Then, the output should be:

11106
'''
#solution 

a=input()
total= int(a)+int(2*a)+int(3*a)+int(4*a)
print(total)

#solution 2

a = input()
total,temp=0,str()

for i in range(4):
    temp+=a
    total+=int(temp)
print(total)
