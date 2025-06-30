"""
Sort by Age
Write a function sort_by_age that takes a list of tuples (name, age) and returns a new
list sorted by age in ascending order. Use a simple sorting algorithm (e.g., bubble sort)
instead of sorted().
Example:

Input: sort_by_age([("Alice", 30), ("Bob", 25), ("Charlie", 35)])
Output: [("Bob", 25), ("Alice", 30), ("Charlie", 35)]
Input: sort_by_age([("Eve", 28), ("Dave", 40)])
Output: [("Eve", 28), ("Dave", 40)]
"""


def sort_by_age(people):
    for i in range(len(people)):
        for j in range(len(people) - 1):
            if people[j][1] > people[j + 1][1]:
                people[j], people[j + 1] = people[j + 1], people[j]
    return people


print(sort_by_age([("Alice", 30), ("Bob", 25), ("Charlie", 35), ("Ram", 12), ("Sita", 1212)]))
print(sort_by_age([("Eve", 28), ("Dave", 40)]))
