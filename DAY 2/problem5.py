'''
Question 5
Question:
Define a class which has at least two methods:

getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
'''

class string_manipulator:
    def __init__(self):
        pass
    def get_string(self):
        self.string=input("Enter a string: ")
    def print_string(self):
        print(self.string.upper())

def test_function():
    sm=string_manipulator()
    sm.get_string()
    sm.print_string()

test_function()
    