"""
Number Pattern Generator (Loops and Conditionals)
Write a function number_pattern(n) that prints a pattern of numbers up to n rows,
where each row contains numbers from 1 to the row number, but only prints odd numbers.
For example, number_pattern(4) should print:

1
1 3
1 3 5
1 3 5 7
Use nested loops and conditionals to check for odd numbers.
"""


def print_odd_pattern(n):
    for row in range(1, n + 1):
        count = 0
        num = 1
        while count < row:
            if num % 2 != 0:
                print(num, end=" ")
                count += 1
            num += 1
        print()


print_odd_pattern(5)
