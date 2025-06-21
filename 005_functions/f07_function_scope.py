# Global variable
x = 10


def my_function():
    # Local variable
    x = 20
    print(f"Inside function: {x}")


my_function()        # Inside function: 20
print(f"Outside: {x}")  # Outside: 10


# Using global keyword
def modify_global():
    global x
    x = 30
    print(f"Inside function: {x}")


modify_global()
print(x)
