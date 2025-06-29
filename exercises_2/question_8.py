import os

file_name = input("Enter a file name: ")

if os.path.exists(file_name):
    print("The file exists!")
else:
    print("The file does not exist.")

print(os.path)
