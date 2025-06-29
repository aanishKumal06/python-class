# Write a Python program to access a function inside a function.

def outer_function(a, b):
    print("Inside outer function")

    def inner_function(x, y):
        return x + y

    result = inner_function(a, b)
    print(f"Sum of {a} and {b} is: {result}")


outer_function(5, 7)
