"""
Filter Even Numbers
Write a function get_evens that takes a list of numbers and returns a new list containing
only the even numbers. Use a loop instead of filter().
Example:

Input: get_evens([1, 2, 3, 4])
Output: [2, 4]
Input: get_evens([5, 6, 7, 8])
Output: [6, 8]
"""


# without filter
def get_evens(numbers):
    even = []
    for num in numbers:
        if num % 2 == 0:
            even.append(num)
    return even


print(get_evens([5, 6, 7, 8]))
print(get_evens([1, 2, 3, 4]))


# with filter
def get_evens_with_filter(numbers):
    return list(filter(lambda x: x % 2 == 0, numbers))


print(get_evens_with_filter([5, 6, 7, 8]))
print(get_evens_with_filter([1, 2, 3, 4]))
