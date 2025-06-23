# Write a Python program to find the common tuples between two given lists.
def find_common_tuples(list1, list2):
    common = []
    for item in list1:
        if item in list2:
            common.append(item)
    return common


list_a = [('red', 'green'), ('black', 'white'), ('orange', 'pink')]
list_b = [('red', 'green'), ('orange', 'pink')]

common_tuples = find_common_tuples(list_a, list_b)
print("Common tuples:", common_tuples)
