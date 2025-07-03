"""
Dictionary Merge (Dictionaries and Conditionals)
Write a function merge_dicts(dict1, dict2) that merges two dictionaries. If a key exists
in both dictionaries, sum their values. For example, merge_dicts({"a": 1, "b": 2}, {"b": 3, "c": 4})
returns {"a": 1, "b": 5, "c": 4}. Use dictionary methods like keys() or items() and conditionals.
"""


def merge_dicts(dict1, dict2):
    for key, value in dict2.items():
        if key in dict1:
            dict1[key] += value
        else:
            print(f"Key {key} not found in dict1, adding it.")
            dict1[key] = value
    return dict1


print(merge_dicts({"a": 1, "b": 2, "z": 4}, {"b": 3, "c": 4}))


# def merge_dicts(dict_one: dict[str, int], dict_two: dict[str, int]) -> dict[str, int]:
#     for key, value in dict_one.items():
#         if key in dict_two:
#             dict_two[key] = dict_one[key] + dict_two[key]
#         else:
#             dict_two[key] = value

#     return dict_two


# dict_one = {"a": 1, "b": 2}
# dict_two = {"b": 5, "c": 2}
# print(merge_dicts(dict_one, dict_two))
