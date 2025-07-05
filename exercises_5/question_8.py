"""
Hollow Diamond Pattern

Task: Print a hollow diamond pattern with 5 rows in the upper half (total 9 rows),
where only the border is made of stars.
Example Output:
    *
   * *
  *   *
 *     *
*       *
 *     *
  *   *
   * *
    *
Hint: Similar to the diamond pattern, but print stars only at the first and last positions
of each row’s star sequence. Manage spaces carefully.

"""


def hollow_diamond(rows):
    for i in range(1, rows + 1):
        if i == 1:
            leading_spaces = ' ' * (rows - i)
            stars = '*' * (i * 2 - 1)
            print(leading_spaces + stars)
        else:
            spaces = ' ' * (rows - i)
            spaces_gap_between_stars = (i * 2 - 3)
            stars_with_space = "*" + " " * spaces_gap_between_stars + "*"
            print(spaces + stars_with_space)
    for i in range(rows - 1, 0, -1):
        if i == 1:
            spaces = ' ' * (rows - i)
            stars = '*' * (i * 2 - 1)
            print(spaces + stars)
        else:
            spaces = ' ' * (rows - i)
            spaces_gap_between_stars = (i * 2 - 3)
            stars_with_space = "*" + " " * spaces_gap_between_stars + "*"
            print(spaces + stars_with_space)


hollow_diamond(10)
