count = 0
while True:
    try:
        number = int(input("ENter a number between 1 and 10: "))
        if 1 <= number <= 10:
            print("Great choice!")
            break
        else:
            count += 1
            print(f"That's not between 1 and 10! Try again: {count}")
    except ValueError:
        print("Invalid input! Try Again!")
