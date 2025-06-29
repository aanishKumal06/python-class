# Write a Python program to remove all values except integer values from a given array of mixed values.
def keep_only_integers(arr):
    result = []
    for item in arr:
        if isinstance(item, int):
            result.append(item)
    return result


mixed_list = [10, "hello", 3.5, 7, True, 42, "world", -5]
filtered_list = keep_only_integers(mixed_list)
print("List with only integers:", filtered_list)
