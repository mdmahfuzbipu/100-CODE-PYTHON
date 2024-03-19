'''
Question:
A website requires the users to input username and password to register. Write a program to check the validity of password input by users.

Following are the criteria for checking the password:

At least 1 letter between [a-z]
At least 1 number between [0-9]
At least 1 letter between [A-Z]
At least 1 character from [$#@]
Minimum length of transaction password: 6
Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.

Example

If the following passwords are given as input to the program:

ABd1234@1,a F1#,2w3E*,2We3345

Then, the output of the program should be:

ABd1234@1
'''

#solution

import re

def check(password):
    if len(password) < 6 or len(password) > 12:
        return False
    if not re.search(r"[a-z]",password):
        return False
    if not re.search(r"[A-Z]",password):
        return False
    if not re.search(r"\d",password):
        return False
    if not re.search(r"[@$#]",password):
        return False
    return True
passwords=input("Enter comma separated passwords: ").split(",") #taking input with separating them by comma as a list
valid_passwords=[]

for password in passwords:
    if check(password):
        valid_passwords.append(password)

print(",".join(valid_passwords))

