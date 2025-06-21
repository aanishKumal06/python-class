# Loop through a list
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f"I like {fruit}")

# Loop through a range
for i in range(5):        # 0 to 4
    print(i)

for i in range(2, 8, 2):  # Start, stop, step
    print(i)              # 2, 4, 6


# for loop with dictionary

student = {"name": "Alice", "age": 20, "grade": "A"}

# Loop through keys
for key in student:
    print(key)

# Loop through values
for value in student.values():
    print(value)

# Loop through key-value pairs
for key, value in student.items():
    print(f"{key}: {value}")
