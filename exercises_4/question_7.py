"""
Dictionary Merge (Dictionaries and Conditionals)
Write a function merge_dicts(dict1, dict2) that merges two dictionaries. If a key exists
in both dictionaries, sum their values. For example, merge_dicts({"a": 1, "b": 2}, {"b": 3, "c": 4})
returns {"a": 1, "b": 5, "c": 4}. Use dictionary methods like keys() or items() and conditionals.
"""


def merge_dicts(dict1, dict2):
    merged = dict1
    for key, value in dict2.items():
        if key in merged:
            merged[key] += value
        else:
            merged[key] = value
    return merged


print(merge_dicts({"a": 1, "b": 2}, {"b": 3, "c": 4}))
