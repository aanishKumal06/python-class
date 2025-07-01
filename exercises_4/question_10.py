"""
List Range Filter (Lists, Loops, and Conditionals)
Write a function filter_range(lst, min_val, max_val) that takes a list of numbers and
returns a new list containing only the numbers within the range [min_val, max_val] (inclusive).
For example, filter_range([1, 5, 3, 8, 2], 2, 5) returns [5, 3, 2]. Use list methods
like append() and loops with conditionals.
"""


def filter_range(lst, min_val, max_val):
    result = []
    for num in lst:
        if min_val <= num <= max_val:
            result.append(num)
    return result


print(filter_range([1, 5, 3, 8, 2], 2, 5))
