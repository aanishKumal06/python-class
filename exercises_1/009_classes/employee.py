class Employee:
    def __init__(self):
        self.employees = {
            "E01": {"name": "ADAMS", "salary": 50000, "department": "ACCOUNTING"},
            "E02": {"name": "JONES", "salary": 45000, "department": "RESEARCH"},
            "E03": {"name": "MARTIN", "salary": 50000, "department": "SALES"},
            "E04": {"name": "SMITH", "salary": 55000, "department": "OPERATIONS"},
        }

    def calculate_emp_salary(self):
        emp_id = input("Enter Employee ID: ")
        emp = self.employees.get(emp_id)
        if not emp:
            print("Employee ID not found.")
            return

        try:
            overtime = float(input("Enter overtime: "))
            if overtime < 0:
                print("Overtime cannot be negative.")
                return
        except ValueError:
            print("Invalid input for hours worked. Please enter a number.")
            return

        base_salary = emp['salary']

        overtime_pay = overtime * (base_salary / 50)
        total_salary = base_salary + overtime_pay

        print(f"\nBase salary: Rs.{base_salary:.2f}")
        print(f"Overtime hours: {overtime}")
        print(f"Overtime pay: Rs.{overtime_pay:.2f}")
        print(f"Total salary (with overtime): Rs.{total_salary:.2f}")

    def change_department(self):
        emp_id = input("Enter Employee ID: ")
        emp = self.employees.get(emp_id)
        if not emp:
            print("Employee ID not found.")
            return
        else:
            new_dept = input("Enter new Department: ")
            emp['department'] = new_dept
            print(f"Department updated for {emp['name']}.")

    def print_employee_details(self):
        print("\nEmployee Details:")
        for emp_id, info in self.employees.items():
            print(f"ID: {emp_id}")
            print(f"Name: {info['name']}")
            print(f"Salary: Rs.{info['salary']:.2f}")
            print(f"Department: {info['department']}")
            print("-" * 30)

    def menu(self):
        print("\n===== EMPLOYEE MENU =====")
        print("1. Show all employees")
        print("2. Calculate employee salary")
        print("3. Assign employee department")
        print("4. Exit")

    def run(self):
        while True:
            self.menu()
            choice = input("Enter choice (1-4): ")
            if choice == '1':
                self.print_employee_details()
            elif choice == '2':
                self.calculate_emp_salary()
            elif choice == '3':
                self.change_department()
            elif choice == '4':
                print("Exiting Employee Management. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


emp_system = Employee()
emp_system.run()
