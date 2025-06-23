# Write a Python program to find the smallest and largest words in a given string.
def swap_case_string(s):
    result = ""
    for char in s:
        if char.isupper():
            result += char.lower()
        else:
            result += char.upper()
    return result


user_input = input("Enter a string: ")

print("Swapped case string:", swap_case_string(user_input))
