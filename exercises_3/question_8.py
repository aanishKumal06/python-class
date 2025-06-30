"""
Double List Elements
Write a function double_list that takes a list of numbers and returns a new list where each
element is doubled. Use a loop .
Example:

Input: double_list([1, 2, 3])
Output: [2, 4, 6]
Input: double_list([5, 10])
Output: [10, 20]
"""


# without map
def double_list(numbers):
    double = []
    for num in numbers:
        double.append(num * 2)
    return double


print(double_list([1, 2, 3]))
print(double_list([5, 10]))


# with map
def double_list_with_map(numbers):
    return list(map(lambda x: x * 2, numbers))


print(double_list_with_map([1, 2, 3]))
print(double_list_with_map([5, 10]))
