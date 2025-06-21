# Global list to store fruit names
fruits = []


# Function to add fruits to the list
def add_fruits():
    global fruits  # allows modifying the global list
    count = int(input("How many fruits do you want to add: "))
    while count > 0:
        fruit_name = input("Enter fruit name: ")
        fruits.append(fruit_name)
        count -= 1
    print("All the fruits have been added successfully.")


# Function to display all fruits with their index
def display_fruits():
    print("\nThe list of fruits is given below:")
    for i, fruit in enumerate(fruits):
        print(f"{i}: {fruit}")  # shows index and fruit name


# Function to update a fruit at a specific index
def update_fruit():
    global fruits
    display_fruits()
    update_index = int(input("Enter the index number to update: "))
    update_value = input("Enter the new fruit name: ")
    if 0 <= update_index < len(fruits):  # check if index is valid
        fruits[update_index] = update_value
        print("Fruit updated successfully.")
    else:
        print("Invalid index.")


# Function to delete a fruit at a specific index
def delete_fruits():
    global fruits
    display_fruits()
    deletion_index = int(input("Enter the index to delete: "))
    if 0 <= deletion_index < len(fruits):  # validate index
        removed = fruits.pop(deletion_index)
        print(f"The item '{removed}' at index {deletion_index} was deleted.")
    else:
        print("Invalid index.")


# Function to print the main menu
def menu():
    print("\n========== MENU ==========")
    print("1. Display")
    print("2. Add")
    print("3. Update")
    print("4. Remove")
    print("5. Exit")


# Infinite loop for user interaction
while True:
    menu()  # show menu options
    choice = input("Enter your choice (1-5): ")

    # Match user's choice to functions
    if choice == "1":
        display_fruits()
    elif choice == "2":
        add_fruits()
    elif choice == "3":
        update_fruit()
    elif choice == "4":
        delete_fruits()
    elif choice == "5":
        print("Exiting program. Goodbye!")
        break  # exits the loop and ends the program
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
