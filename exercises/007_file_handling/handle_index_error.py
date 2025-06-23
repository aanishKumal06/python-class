""" Write a Python program that executes an operation on a list and handles an IndexError
 exception if the index is out of range. """


def access_list_element(my_list, index):
    try:
        print("Element at index", index, "is:", my_list[index])
    except IndexError:
        print("IndexError: The index is out of range.")


numbers = [10, 20, 30, 40, 50]

index_of_list = int(input("Enter an index to access: "))
access_list_element(numbers, index_of_list)
