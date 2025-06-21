# String creation
name = "Python"
message = 'Hello World'
multiline = """This is a
multiline string"""

# String operations
greeting = "Hello, " + name  # Concatenation
repeated = "Ha" * 3          # Repetition: "HaHaHa"
length = len(name)           # Length: 6

print(greeting)
print(repeated)
print(length)

# String Methods

text = "  Python Programming  "

# Common string methods
print(text.strip())        # Remove whitespace
print(text.lower())        # Convert to lowercase
print(text.upper())        # Convert to uppercase
print(text.replace("Python", "Java"))  # Replace substring
print(text.split())        # Split into list
