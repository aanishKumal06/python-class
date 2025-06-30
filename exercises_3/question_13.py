"""
Reverse All Strings
Write a function reverse_all that takes a list of strings and returns a new list where each string is reversed.
Example:

Input: reverse_all(["hello", "world"])
Output: ["olleh", "dlrow"]
Input: reverse_all(["python", "code"])
Output: ["nohtyp", "edoc"]
"""


def reverse_all(words):
    return [word[::-1] for word in words]


print(reverse_all(["hello", "world"]))
print(reverse_all(["python", "code"]))
