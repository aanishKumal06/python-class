""" Write a Python function to create and print a list where the values are the squares of
  numbers between 1 and 30 (both included)."""


def print_squares():
    squares = []
    for num in range(1, 31):
        squares.append(num ** 2)
    print(squares)


print_squares()
