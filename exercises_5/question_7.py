"""
Number Triangle Pattern

Task: Print a right-angle triangle where each row contains the row number repeated.
Example Output:
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
Hint: Use the row number as the value to print, repeating it based on the row index.
"""


def number_triangle(rows):
    for i in range(1, rows + 1):
        print(f"{i} " * i)


number_triangle(5)
