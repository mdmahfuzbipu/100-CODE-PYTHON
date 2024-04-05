"""
Question:
Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).

Hints:
Use "for" to iterate the tuple. Use tuple() to generate a tuple from a list.
"""

tpl = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

tpl1=tuple(i for i in tpl if i%2==0)
print(tpl1)


#solution 2

tpl2=tuple(
    filter(lambda x: x%2 == 0,tpl) #lambda func returns 1 if returns true
        ) #filter function only keeps the true/1 values


print(tpl2)