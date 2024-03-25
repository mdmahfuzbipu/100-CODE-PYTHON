'''With a given integral number n, write a program to generate a dictionary that contains (i, i x i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.Suppose the following input is supplied to the program: 8
'''

#solution 1 (for loop)

num=int(input())
ans={}
for i in range(1,num+1):
    ans[i]=i*i
print(ans) 


#solution 2 (dictionary comprehension)
num=int(input())

result_dict={num:num*num for num in range(1,num + 1)}
