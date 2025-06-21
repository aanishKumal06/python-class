# Positional parameters must be passed in the correct sequence
def student_info(roll_number, name):
    return f"Student Roll No: {roll_number}, Name: {name}"


# Correct order of arguments
print(student_info(101, "Hema"))

# If order is wrong, output becomes confusing
print(student_info("Hema", 101))  # Student Roll No: John, Name: 101

# Note: Positional parameters are the most basic type of parameters
# and are required unless they have default values
