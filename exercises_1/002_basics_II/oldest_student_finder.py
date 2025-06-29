""" Write a Python program to find the name of the oldest student in a given dictionary containing the names and ages
of a group of students."""


def oldest_student(students):

    oldest_name = None
    oldest_age = -1

    for name, age in students.items():
        if age > oldest_age:
            oldest_age = age
            oldest_name = name

    print(f"The oldest student is {oldest_name} with {oldest_age} years.")


# Test case 1
oldest_student({"Bernita Ahner": 12, "Kristie Marsico": 11,
                      "Sara Pardee": 14, "Fallon Fabiano": 11,
                      "Nidia Dominique": 15})

# Test case 2
oldest_student({"Nilda Woodside": 12, "Jackelyn Pineda": 12.2,
                      "Sofia Park": 12.4, "Joannie Archibald": 12.6,
                      "Becki Saunder": 12.7})
