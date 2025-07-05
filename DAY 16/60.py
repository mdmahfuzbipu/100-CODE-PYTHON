"""
### **Question**

> **_Write a program to compute:_**


> $f(n)=f(n-1)+100$ when n>0

> and $f(0)=0$


> **_with a given n input by console (n>0)._**

> **_Example:
> If the following n is given as input to the program:_**


> 5


> **_Then, the output of the program should be:_**


> 500


> **_In case of input data being supplied to the question, it should be assumed to be a console input._**

---

### Hints

> **_We can define recursive function in Python._**

---
"""


def func(n):
    if n == 0:
        return 0
    return func(n-1) + 100

print(func(5))