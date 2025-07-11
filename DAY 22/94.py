"""
Question
Write a program to solve a classic ancient Chinese puzzle:
We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?

Hints
Use for loop to iterate all possible solutions.
"""

for rabbits in range(1,36):
    chickens = 35 - rabbits
    
    if chickens * 2 + rabbits * 4 == 94:
        print("chickens", chickens, "rabbits", rabbits)