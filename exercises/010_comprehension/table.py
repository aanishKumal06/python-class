""" Write a Python program using list comprehension that takes a number as input from the user
and prints the multiplication table of that number"""

try:
    num = int(input("Enter a number to generate its multiplication table: "))
    table = [f"{num} * {i} = {num * i}"for i in range(1, 11)]
    for line in table:
        print(line)
except ValueError:
    print("Invalid input!")
