fruits = ["apple", "banana", "orange", "grape", "strawberry"]

for index, fruit in enumerate(fruits, start=1):
    if index % 2 != 0:
        print(f"{index}. {fruit}")
