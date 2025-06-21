# Basic try-except
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"The result is {result}.")
except ValueError:
    print("Invalid number.")
except ZeroDivisionError:
    print("Number cannot divide by 0")
