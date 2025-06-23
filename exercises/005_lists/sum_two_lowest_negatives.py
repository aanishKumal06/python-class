# Write a Python program to calculate the sum of two lowest negative numbers in a given array of integers.

def sum_two_lowest_negatives(arr):
    negatives = []
    for num in arr:
        if num < 0:
            negatives.append(num)

    if len(negatives) < 2:
        return "Not enough negative numbers"

    negatives.sort()
    return negatives[0] + negatives[1]


numbers = [5, -1, -8, 3, -6, 0, -10]
result = sum_two_lowest_negatives(numbers)
print("Sum of two lowest negative numbers:", result)
