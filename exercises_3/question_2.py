"""
Palindrome Check
Create a function is_palindrome that takes a string and returns True if it is a palindrome
(reads the same forwards and backwards), False otherwise. Ignore case and non-alphabetic characters.
Example:

Input: is_palindrome("A man a plan a canal Panama")
Output: True
Input: is_palindrome("hello")
Output: False
"""


def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]


user_input = input("Enter a string: ")
if is_palindrome(user_input):
    print(f"'{user_input}' is a palindrome.")
else:
    print(f"'{user_input}' is a palindrome.")
