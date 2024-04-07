"""
Question:
Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No".

Hints:
Use if statement to judge condition.
"""

text=input("Enter a string: ")

output= "".join(["Yes" if text == "yes" or text =="YES" or text == "Yes" else "NO"])

print(str(output))