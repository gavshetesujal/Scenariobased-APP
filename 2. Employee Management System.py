class Employee:
    def __init__(self, employee_id, name, salary):
        self.employee_id = employee_id
        self.name = name
        self.salary = salary

    def get_category(self):
        if self.salary >= 70000:
            return "High Salary"
        elif self.salary >= 40000:
            return "Medium Salary"
        else:
            return "Low Salary"

    def display(self):
        print("Employee ID:", self.employee_id)
        print("Name:", self.name)
        print("Salary: ₹", self.salary)
        print("Category:", self.get_category())
        print("------------------------")


class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee_id, name, salary):
        employee = Employee(employee_id, name, salary)
        self.employees.append(employee)

    def display_all_employees(self):
        print("Employee Information")
        print("========================")

        for employee in self.employees:
            employee.display()


# Main program
company = Company()

# Adding employees
company.add_employee(101, "Rahul", 75000)
company.add_employee(102, "Priya", 55000)
company.add_employee(103, "Amit", 35000)
company.add_employee(104, "Sneha", 70000)
company.add_employee(105, "Karan", 45000)

# Display all employees
company.display_all_employees()
