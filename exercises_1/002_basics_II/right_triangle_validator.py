
def right_triangle_validator(a, b, c):
    list_of_sides = [a, b, c]
    list_of_sides.sort()
    if list_of_sides[0]**2 + list_of_sides[1]**2 == list_of_sides[2]**2:
        print("This is right angle tringle.")
    else:
        print("This is not right angle tringle.")


try:
    x = float(input("Enter the first side: "))
    y = float(input("Enter the second side: "))
    z = float(input("Enter the third side: "))
    right_triangle_validator(x, y, z)
except ValueError:
    print("Invalid input. Please enter numeric values.")
