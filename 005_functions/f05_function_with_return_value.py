# Function that returns a calculated value
def multiply_numbers(x, y):
    return x * y


product = multiply_numbers(4, 6)
print(product)


# Function with a default parameter
def welcome_message(name, message="Welcome"):
    return f"{message}, {name}!"


print(welcome_message("Sita"))
print(welcome_message("Ram", "Good Morning"))
