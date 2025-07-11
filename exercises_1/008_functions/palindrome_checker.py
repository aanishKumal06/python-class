# Write a Python function that checks whether a passed string is a palindrome or not.

def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]


user_input = input("Enter a string: ")
if is_palindrome(user_input):
    print(f"'{user_input}' is a palindrome.")
else:
    print(f"'{user_input}' is not a palindrome.")
