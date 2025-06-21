"""
Q1. Age Group Checker
Checks which age group a person belongs to based on input.
"""


def age_group_checker():
    print("\n--- Age Group Checker ---")
    age = int(input("Enter your age: "))

    # Check age ranges and print appropriate group
    if age > 0 and age < 13:
        print("Child")
    elif age >= 13 and age <= 19:
        print("Teenager")
    elif age >= 20 and age <= 59:
        print("Adult")
    elif age >= 60:
        print("Senior")
    else:
        print("Invalid age")  # For negative or zero input


"""
Q2. Number Operations
Takes two numbers and performs basic operations on them.
"""


def number_operations():
    print("\n--- Number Operations ---")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    # Arithmetic operations
    print("Sum:", num1 + num2)
    print("Difference:", num1 - num2)
    print("Product:", num1 * num2)

    # Divisibility check
    if num2 != 0 and num1 % num2 == 0:
        print(f"{num1} is divisible by {num2}")
    elif num2 != 0:
        print(f"{num1} is not divisible by {num2}")
    else:
        print("Cannot divide by zero.")


"""
Q3. Odd or Even with a Twist
Identifies if the number is odd or even, then prints its square or cube.
"""


def odd_even_twist():
    print("\n--- Odd or Even with a Twist ---")
    number = int(input("Enter a number: "))

    if number % 2 == 0:
        print(f"Even number is {number} and its square is: {number ** 2}")
    else:
        print(f"Odd number is {number} and its cube is: {number ** 3}")


"""
Q4. Sum of N Natural Numbers
Calculates the sum of first n natural numbers using a loop.
"""


def sum_of_n_numbers():
    print("\n--- Sum of N Natural Numbers ---")
    n = int(input("Enter a number: "))
    total = 0

    for i in range(1, n + 1):
        total += i

    print(f"Sum of first {n} natural numbers is: {total}")


"""
Q5. Multiplication Table Generator
Prints multiplication table from 1 to 10 for a given number.
"""


def multiplication_table():
    print("\n--- Multiplication Table Generator ---")
    num = int(input("Enter a number for multiplication table: "))

    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")


# Main menu loop to let user choose tasks
while True:
    print("\n========== MENU ==========")
    print("1. Age Group Checker")
    print("2. Number Operations")
    print("3. Odd or Even with a Twist")
    print("4. Sum of N Natural Numbers")
    print("5. Multiplication Table Generator")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    # Match choice with function calls
    if choice == "1":
        age_group_checker()
    elif choice == "2":
        number_operations()
    elif choice == "3":
        odd_even_twist()
    elif choice == "4":
        sum_of_n_numbers()
    elif choice == "5":
        multiplication_table()
    elif choice == "6":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
