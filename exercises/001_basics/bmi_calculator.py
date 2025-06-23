# Write a Python program to calculate the body mass index.

try:
    # Get user input
    weight = float(input("Enter your weight in kilograms : "))
    height = float(input("Enter your height in meters : "))

    if weight <= 0 or height <= 0:
        print("Weight and height must be positive numbers and more than zero.")
    else:

        bmi = weight / (height ** 2)
        print(f"Your BMI is: {bmi:.2f}")

        if bmi < 18.5:
            print("Underweight")
        elif 18.5 <= bmi < 24.9:
            print("Normal weight")
        elif 25 <= bmi < 29.9:
            print("Overweight")
        elif 30 <= bmi < 34.9:
            print("Obese")
        else:
            print("Extermely Obese")

except ValueError:
    print("Invalid input. Please enter numeric values for weight and height.")
