"""
Question
Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the company name of a given email address. Both user names and company names are composed of letters only.

Example:
If the following email address is given as input to the program:

john@google.com

Then, the output of the program should be:

google

In case of input data being supplied to the question, it should be assumed to be a console input.

Hints
Use \w to match letters.
"""
import re

email = "mahfuz@kahf.com ronaldo@meta.com sakib@openai.com"
pattern = r"\w+@(\w+).com"
company_name = re.findall(pattern, email)
print(company_name)