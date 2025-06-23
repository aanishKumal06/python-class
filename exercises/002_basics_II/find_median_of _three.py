# Write a Python program to find the median among three given numbers.

def find_median(a, b, c):
    numbers = [a, b, c]
    numbers.sort()  # Sorts the list in ascending order
    return numbers[1]


try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))

    median = find_median(num1, num2, num3)
    print(f"The median is: {median}")

except ValueError:
    print("Invalid input. Please enter numeric values.")
