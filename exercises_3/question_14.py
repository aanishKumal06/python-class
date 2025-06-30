"""
Sum of Arguments
Create a function sum_all that accepts any number of numeric arguments and returns their
sum. Use *args for variable arguments.
Example:

Input: sum_all(1, 2, 3)
Output: 6
Input: sum_all(10, 20)
Output: 30
"""


def sum_all(*args):
    return sum(args)


print(sum_all(1, 2, 3))
print(sum_all(10, 20))
