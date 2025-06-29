"""Write a Python program that prompts the user to input an integer and raises a ValueError
exception if the input is not a valid integer."""


def sum_of_n_numbers():
    print("Sum of N Natural Numbers")
    try:
        n = int(input("Enter a number: "))
        if n < 1:
            print("Please enter a positive integer.")
            return
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
        return

    total = 0
    for i in range(1, n + 1):
        total += i

    print(f"Sum of first {n} natural numbers is: {total}")


sum_of_n_numbers()
