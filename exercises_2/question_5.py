try:
    temp = float(input("Enter the temperature:  "))
    if temp > 30:
        print("It's hot! Wear sunglasses")
    elif 15 <= temp <= 30:
        print("It's nice outside! Enjoy!")
    else:
        print("It's cold! Wear a jacket!")
except ValueError:
    print("Invalid input! Try Again!")
