# Basic while loop
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1

# While with condition
password = ""
while password != "secret":
    password = input("Enter password: ")
    if password != "secret":
        print("Wrong password!")
