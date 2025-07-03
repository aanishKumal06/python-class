"""
Hollow Right-Angle Triangle

Task: Print a hollow right-angle triangle with 5 rows, where only the border is made of stars.
Example Output:
*
**
* *
*  *
*****
Hint: For each row, print stars only at the first position, last position, and in the last row fully.
"""


def hollow_right_triangle(rows):
    for i in range(1, rows + 1):
        if i == 1 or i == rows:
            print('*' * i)
        else:
            spaces = ' ' * (i - 2)
            print('*' + spaces + '*')


hollow_right_triangle(5)
