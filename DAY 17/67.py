"""
Question
Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.

Hints
Use if/elif to deal with conditions.
"""

def binary_search(numbers, x):
    upper = len(numbers) - 1
    lower = 0
    
    while lower <= upper:
        mid = lower + (upper - lower) // 2
        
        if numbers[mid] == x:
            return mid
        
        elif numbers[mid] > x:
            upper = mid - 1
        elif numbers[mid] < x:
            lower = mid + 1
            
    return -1


numbers = [1,4,6,7,8,22]
x = 4

index = binary_search(numbers, x)

if index == -1:
    print("The number is not present in the list")
else:
    print("The number is at", index+1,"th position in the array")