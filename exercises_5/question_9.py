"""
Pascal’s Triangle Pattern

Task: Print the first 5 rows of Pascal’s triangle using numbers.
Example Output:
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
Hint: Use the binomial coefficient formula or precompute values. Focus on spacing to
align the numbers centrally.
"""


def pascals_triangle(rows):
    for i in range(rows):
        print(' ' * (rows - i), end='')

        num = 1
        for j in range(0, i + 1):
            print(num, end=' ')
            num = num * (i - j) // (j + 1)
        print()


pascals_triangle(5)
