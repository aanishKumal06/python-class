# Write a Python program to print a dictionary line by line.

students = {
    'Ram': {'class': 10, 'roll_id': 2},
    'Puja': {'class': 9, 'roll_id': 3}
}

for name, details in students.items():
    print(f"Student: {name}")
    for key, value in details.items():
        print(f"{key}: {value}")
    print()
