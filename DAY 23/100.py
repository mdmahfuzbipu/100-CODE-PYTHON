"""
Question
You are given words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification.

If the following string is given as input to the program:

4
bcdef
abcdefg
bcde
bcdef

Then, the output of the program should be:

3
2 1 1

Hints
Make a list to get the input order and a dictionary to count the word frequency
"""

n=int(input())

word_counts = {}
order = []

for _ in range(n):
    word = input()
    
    if word in word_counts:
        word_counts[word] += 1
    
    else:
        word_counts[word] = 1
        order.append(word)

print(len(order))