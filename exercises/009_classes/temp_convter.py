class Temp_Convter:

    def c_to_f(self):
        try:
            temp = int(input("Input the temp in Celsius (°C): "))
            f = (temp * 9 / 5) + 32
            print(f"{temp}°C Celsius is equal to {f}°F Fahrenheit. ")
        except ValueError:
            print("Invalid input")

    def f_to_c(self):
        try:
            temp = int(input("Input the temp in Fahrenheit (°F): "))
            c = (temp - 32) * 5 / 9
            print(f"{temp}°F Fahrenheit is equal to {c}°C Celsius. ")
        except ValueError:
            print("Invalid input")

    def menu(self):
        print("\n===== Convter MENU =====")
        print("1. Celsius (°C) to Fahrenheit (°F)")
        print("2. Fahrenheit (°F) to Celsius (°C) ")
        print("3. Exit")

    def run(self):
        while True:
            self.menu()
            choice = input("Enter choice (1-3): ")
            if choice == '1':
                self.c_to_f()
            elif choice == '2':
                self.f_to_c()
            elif choice == '3':
                print(" Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


temp_convter = Temp_Convter()
temp_convter.run()
