# Write a Python program to swap two variables.

a = 112
b = 343
print(f"Before swap a = {a} and b = {b}")
a, b = b, a
print(f"After swap a = {a} and b = {b}")

# alternative

x = 100
y = 200
print(f"Before swap x = {x} and y = {y}")

x = x + y
y = x - y
x = x - y
print(f"After swap x = {x} and y = {y}")
