file = open("introduction.txt", "w+")
file.write("My name is Anish Kumal.\n")
file.write("I live in lekhnath.")

file.seek(0)
lines = file.readlines()

for line in lines:
    print(line, end="")


with open("introduction.txt", "w+") as file:
    file.write("My name is Anish Kumal.\n")
    file.write("I live in lekhnath")

    file.seek(0)
    lines = file.readlines()

    for line in lines:
        print(line, end="")
