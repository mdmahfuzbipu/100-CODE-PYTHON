"""
Question
Please write a program to print the running time of execution of "1+1" for 100 times.

Hints
Use timeit() function to measure the running time.
"""

import time

before = time.time()  # Record time before the loop
for i in range(100000):  # Run your code 100 times
    x = 1 + 1
after = time.time()  # Record time after the loop

execution_time = after - before  # Total duration in seconds
print(execution_time)
