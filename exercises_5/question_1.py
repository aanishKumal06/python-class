"""
Right-Angle Triangle Pattern

Task: Write a Python program to print a right-angle triangle of stars with 5 rows.
Example Output:
*
**
***
****
*****
Hint: Use a single for loop to control the number of stars in each row, increasing from 1 to 5.
"""


def right_angle_triangle(rows):
    for i in range(1, rows + 1):
        print("*" * i)


right_angle_triangle(5)
