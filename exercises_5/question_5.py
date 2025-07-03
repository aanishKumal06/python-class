"""
Diamond Pattern

Task: Print a diamond pattern of stars with 5 rows in the upper half (total 9 rows).
Example Output:
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
Hint: Combine the logic of a centered triangle (increasing stars) and an inverted centered
triangle (decreasing stars). Use two separate loops or a conditional approach.t.
"""


def diamond_pattern(rows):
    for i in range(1, rows + 1):
        spaces = ' ' * (rows - i)
        stars = '*' * (i * 2 - 1)
        print(spaces + stars)
    for i in range(rows - 1, 0, -1):
        spaces = ' ' * (rows - i)
        stars = '*' * (i * 2 - 1)
        print(spaces + stars)


diamond_pattern(5)
