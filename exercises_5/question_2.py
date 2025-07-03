"""
Inverted Right-Angle Triangle Pattern

Task: Print an inverted right-angle triangle of stars with 5 rows.
Example Output:
*****
****
***
**
*
Hint: Decrease the number of stars from 5 to 1 as the row number increases.
"""


def inverted_right_angle_triangle(rows):
    for i in range(rows, 0, -1):
        print("*" * i)


inverted_right_angle_triangle(5)
