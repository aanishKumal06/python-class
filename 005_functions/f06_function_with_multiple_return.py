def get_student_info(name, age):
    greeting = f"Hello, {name}!"
    is_adult = age >= 18
    return greeting, is_adult


# Unpack the returned tuple
message, adult_status = get_student_info("Hema", 19)
print(f"{message} Adult: {adult_status}")

# Or keep as tuple
info = get_student_info("Hema", 19)
print(info)
