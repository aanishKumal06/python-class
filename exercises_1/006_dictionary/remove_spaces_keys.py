# Write a Python program to remove spaces from dictionary keys.

def remove_spaces_from_keys(d):
    result = {}
    for key, value in d.items():
        new_key = key.replace(" ", "")
        result[new_key] = value
    return result


my_dict = {'first name': 'Hema', 'last name': 'Grg', 'age': 25}
cleaned_dict = remove_spaces_from_keys(my_dict)

print("Dictionary with spaces removed from keys:")
print(cleaned_dict)
