age = 25
has_license = True

# Logical operators
if age >= 18 and has_license:
    print("Can drive")

if age < 16 or not has_license:
    print("Cannot drive alone")

# Membership operators
fruits = ["apple", "banana", "orange"]
if "apple" in fruits:
    print("We have apples!")
