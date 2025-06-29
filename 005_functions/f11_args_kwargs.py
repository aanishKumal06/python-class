# packing

def multiply(*args):
    product = 1

    for item in args:
        product = product * item

    return product


result = multiply(1, 2, 3, 4, 5, 6)
print(result)


def greet(**kwargs):

    first_name = kwargs.get("first_name")
    print(f"My first name is {first_name}")

    for key, value in kwargs.items():
        if key == "first_name":
            print(f"Hello {value}")
        else:
            print(value)


greet(first_name="Anish", last_name="Kumal", middle_name="Bdr")
