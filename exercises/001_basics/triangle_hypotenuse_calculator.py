from math import sqrt

# Write a Python program to calculate the hypotenuse of a right angled triangle.
try:
    height = float(input("Enter the height of a right angled triangle: "))
    base = float(input("Enter the base of a right angled triangle: "))
    hypotenuse = (height**2 + base**2)**0.5
    # another way
    hypotenuse_with_sqrt = sqrt(height**2 + base**2)
    print(f"The hypotenuse of a right angled triangle is: {hypotenuse:.2f}")
    print(f"The hypotenuse of a right angled triangle is: {hypotenuse_with_sqrt:.2f}")
except ValueError:
    print("Invalid !!, Please enter numeric values for height and base.")
