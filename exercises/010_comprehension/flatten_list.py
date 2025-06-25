# Convert 2D list to 1D list with Help of list comprehesion
two_d_list = [[1, 2], [3, 4], [5, 6]]
one_d_list = [num for sublist in two_d_list for num in sublist]
print(one_d_list)
