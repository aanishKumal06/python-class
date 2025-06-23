# Write a Python program to combine two dictionary by adding values for common keys

def combine_dicts(d1, d2):
    for key in d2:
        if key in d1:
            d1[key] += d2[key]  # Add values if key exists in both
        else:
            d1[key] = d2[key]   # Otherwise, just set the value
    return d1


dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 5, 'c': 15, 'd': 25}

combined = combine_dicts(dict1, dict2)
print("Combined dictionary:", combined)
