"""
Write a Python program that takes a list of words and groups them based on their length. The program should create a dictionary where:
•	The keys are the lengths of the words (as numbers),
•	The values are lists of words having that length.
Finally, print the dictionary.

Example Input:
words = ["apple", "dog", "banana", "car", "cat"]

Expected Output:
{
  5: ['apple'],
  3: ['dog', 'car', 'cat'],
  6: ['banana']
}

"""

words = ["apple", "dog", "banana", "car", "cat"]
grouped = {}

for word in words:
    length = len(word)
    if length not in grouped:
        grouped[length] = []
    else:
        grouped[length].append(word)

print(grouped)
