'''Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line.'''

#solution 1
lst=[]

for num in range(200,3201):
    if num % 7 == 0  and num % 5 != 0:
        lst.append(str(num)) #join() method expects a sequence of strings because cannot directly join integers

print(",".join(lst))

#solution 2

for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        print(i, end=",")
print("\b") # here /b is for backspace and also it removes the last comma or whatever is the last sequence

#Solution 3
#generator expression
print(*(i for i in range(2000,3201) if i % 7 == 0 and i % 5 != 0), sep=",") # here * operator is used to unpack

# examples of generator expression
squares = (x ** 2 for x in range(1, 6))
squares_list = list(squares) #here list() iterates all the values and store them
print(squares_list) 


#solution 4
#list comprehension 

numbers=[i for i in range(2000,3201) if i % 7 == 0 and i % 5 != 0]

print(*numbers, sep=",")

#  (*) operator is used before an iterable (such as a list)
#  it unpacks the elements of the iterable. In this case, it unpacks the elements of the numbers list.