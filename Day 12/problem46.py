"""
Question:
Define a class named American and its subclass NewYorker.

Hints:
Use class Subclass(ParentClass) to define a subclass.*
"""

class American:
    print("He lives in America")

class NewYorker(American):
    print("Lives in NewYork")


man = American()
man2 = NewYorker()

print(man)
print(man2)
