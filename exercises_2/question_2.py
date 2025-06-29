try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("Sum", num1 + num2)
    print("Product:", num1 * num2)
except ValueError:
    print("Invalid input! Try Again!")
