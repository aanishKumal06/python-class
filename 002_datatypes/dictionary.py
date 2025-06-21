# Key-value pairs
student = {
    "name": "Hema",
    "age": 20,
    "grade": "A",
    "courses": ["Math", "Physics"]
}

# Accessing values
print(student["name"])           # "Hema"
print(student.get("age"))        # 20
print(student.get("height", 0))  # 0 (default value)

# Dictionary Methods
student1 = {"name": "Hema", "age": 20}

# Adding/updating
student1["grade"] = "A"           # Add new key
student1.update({"city": "NYC"})  # Add multiple

print(student1)

# Removing
del student1["age"]               # Remove key
grade = student1.pop("grade")     # Remove and return

# Useful methods
print(student1.keys())            # Get all keys
print(student1.values())          # Get all values
