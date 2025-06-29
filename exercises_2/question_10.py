import random

try:
    rolls = int(input("How many times do you want to roll the die? "))
    for i in range(1, rolls + 1):
        print(f"Roll {i}: {random.randint(1, 6)}")
except ValueError:
    print("Invalid input! Try Again!")
