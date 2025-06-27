"""
Question:
Define a class named American which has a static method called printNationality.

Hints:
Use @staticmethod decorator to define class static method.There are also two more methods.
"""

class American:
    @staticmethod
    def printNationality():
        print("Method is runnning without self parameter as static method is used")
        

American.printNationality()