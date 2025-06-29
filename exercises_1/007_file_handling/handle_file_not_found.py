# Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.

def open_file(filename):
    try:
        with open(filename, 'r') as fp:
            content = fp.read()
        print("File content:")
        print(content)
    except FileNotFoundError:
        print(f"FileNotFoundError: The file '{filename}' does not exist.")


file_name = input("Enter the file name to open: ")
open_file(file_name)
