class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"{self.emp_id} {self.name} {self.age} {self.salary}"


class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def print_employee_data(self):
        for employee in self.employees:
            print(employee)

    def sort_employees(self, sort_option):
        if sort_option == 1:
            self.employees.sort(key=lambda x: x.age)
        elif sort_option == 2:
            self.employees.sort(key=lambda x: x.name)
        elif sort_option == 3:
            self.employees.sort(key=lambda x: x.salary)
        else:
            print("Invalid sorting option.")

    def menu(self):
        while True:
            print("\nMenu:")
            print("1. Add Employee")
            print("2. Print Employee Data")
            print("3. Sort Employees")
            print("4. Exit")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                emp_id = input("Enter Employee ID: ")
                name = input("Enter Name: ")
                age = int(input("Enter Age: "))
                salary = float(input("Enter Salary: "))
                employee = Employee(emp_id, name, age, salary)
                self.add_employee(employee)
                print("Employee added successfully.")
            elif choice == 2:
                self.print_employee_data()
            elif choice == 3:
                sort_option = int(input("Select sorting parameter (1. Age, 2. Name, 3. Salary): "))
                self.sort_employees(sort_option)
                print("Employees sorted successfully.")
            elif choice == 4:
                break
            else:
                print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    company = Company()
    company.menu()
