# Creating lists
fruits = ["apple", "banana", "orange", "cherry", "mango"]
numbers = [1, 2, 3, 4, 5]
mixed = ["hello", 42, True, 3.14]

# Accessing elements
print(fruits[0])    # "apple" (first element)
print(fruits[-1])   # "mango" (last element)
print(fruits[1:3])  # ["banana", "orange"] (slicing)

# List Methods

# Adding elements
fruits.append("orange")      # Add to end
fruits.insert(1, "grape")   # Insert at index

# Removing elements
fruits.remove("banana")      # Remove by value
popped = fruits.pop()        # Remove and return last

# Other operations
print(len(fruits))           # Length
fruits.sort()               # Sort in place
print(fruits)
