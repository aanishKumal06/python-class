"""
Personal Details
Write a function print_details that takes three parameters: name, age, and city,
and prints them in the format "Name: [name], Age: [age], City: [city]". Call this function
using keyword arguments.
Example:

Input: print_details(name="Bob", age=30, city="New York")
Output: Name: Bob, Age: 30, City: New York
Input: print_details(city="London", name="Alice", age=25)
Output: Name: Alice, Age: 25, City: London
"""


def print_details(name, age, city):
    print(f"Name: {name}, Age: {age}, City: {city}")


print_details(name="Bob", age=30, city="New York")
print_details(city="London", name="Alice", age=25)
