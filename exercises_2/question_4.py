while True:
    try:
        number = int(input("ENter a number between 1 and 10: "))
        if 1 <= number <= 10:
            print(f"Great choice! {number}")
            break
        else:
            print(f"That's not between 1 and 10! Try again: {number}")
    except ValueError:
        print("Invalid input! Try Again!")
