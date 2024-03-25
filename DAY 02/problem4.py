'''Question 4:
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.Suppose the following input is supplied to the program:
'''

nums=input("Enter comma-separated numbers:")
sep_num=nums.split(',')

num_list=list(sep_num)
num_tuple=tuple(sep_num)
print(num_list)
print(num_tuple)

#alternate solution

lst=input().split(',')
# the input is being taken as string and as it is string it has a built in
# method name split. ',' inside split function does split where it finds any ','
# and save the input as list in lst variable
tup=tuple(lst)
print(lst)
print(tup)