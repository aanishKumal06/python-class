num1 = int(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /, %, **): ")
num2 = int(input("Enter second number: "))

if operator == "+":
    operation = num1 + num2
    print(f"The sum of {num1} and {num2} is {operation}.")
elif operator == "-":
    operation = num1 - num2
    print(f"The difference of {num1} and {num2} is {operation}.")
elif operator == "*":
    operation = num1 * num2
    print(f"The multiplication of {num1} and {num2} is {operation}.")
elif operator == "**":
    operation = num1 ** num2
    print(f"The power of {num1} raised to {num2} is {operation}.")
elif operator == "/":
    operation = num1 / num2
    print(f"The division of {num1} by {num2} is {operation}.")
elif operator == "%":
    operation = num1 % num2
    print(f"The modulus of {num1} and {num2} is {operation}.")
else:
    print("Invalid operator.")
