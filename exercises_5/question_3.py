"""
Centered Triangle (Pyramid) Pattern

Task: Print a centered triangle of stars with 5 rows, using spaces to align the stars.
Example Output:
    *
   ***
  *****
 *******
*********
Hint: For each row, calculate the number of spaces needed before the stars to center the
pattern, and use an odd number of stars (1, 3, 5, etc.).
"""


# def centered_triangle(num):
#     for i in range(1, num + 1, 2):
#         spaces = ' ' * ((num - i) // 2)
#         stars = '*' * i
#         print(spaces + stars)


# centered_triangle(5)


def centered_triangle(rows):
    for i in range(1, rows + 1):
        spaces = ' ' * (rows - i)
        stars = '*' * (i * 2 - 1)
        print(spaces + stars)


centered_triangle(5)
