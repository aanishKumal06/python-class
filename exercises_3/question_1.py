"""
Reverse a String
Write a function reverse_string that takes a string as input and returns the string reversed.
Example:

Input: reverse_string("hello")
Output: "olleh"
Input: reverse_string("Python")
Output: "nohtyP"
"""


def reverse_string(s):
    return s[::-1]


user_input = input("Enter a string: ")
print(reverse_string(user_input))
