"""
Dictionary Key-Value Inverter (Dictionaries)
Write a function invert_dict(d) that inverts a dictionary, making keys into values and
values into keys. If multiple keys have the same value, group those keys in a list as
the new value. For example, invert_dict({"a": 1, "b": 2, "c": 1})
returns {1: ["a", "c"], 2: ["b"]}. Use dictionary methods like items() and loops.
"""


def invert_dict(d):
    inverted = {}
    for key, value in d.items():
        if value not in inverted:
            inverted[value] = [key]
        else:
            inverted[value].append(key)
    return inverted


print(invert_dict({"a": 1, "b": 2, "c": 1}))
