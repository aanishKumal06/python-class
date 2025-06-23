# Write a Python program to count Uppercase, Lowercase, special characters and numeric values in a given string.
def count_characters(s):
    uppercase_count = 0
    lowercase_count = 0
    digit_count = 0
    special_count = 0

    for char in s:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
        elif char.isdigit():
            digit_count += 1
        else:
            special_count += 1

    return uppercase_count, lowercase_count, digit_count, special_count


input_string = input("Enter a string: ")
upper, lower, digits, special = count_characters(input_string)

print(f"Uppercase letters: {upper}")
print(f"Lowercase letters: {lower}")
print(f"Digits: {digits}")
print(f"Special characters: {special}")
