"""
Inverted Centered Triangle Pattern

Task: Print an inverted centered triangle of stars with 5 rows.
Example Output:
*********
 *******
  *****
   ***
    *
Hint: Start with the maximum number of stars and decrease them, while increasing the
leading spaces for alignment.
"""

# def inverted_centered_triangle(num):
#     for i in range(num, 0, -2):
#         spaces = ' ' * ((num - i) // 2)
#         stars = '*' * i
#         print(spaces + stars)


# inverted_centered_triangle(5)


def inverted_centered_triangle(rows):
    for i in range(rows, 0, -1):
        spaces = ' ' * (rows - i)
        stars = '*' * (i * 2 - 1)
        print(spaces + stars)


inverted_centered_triangle(5)
