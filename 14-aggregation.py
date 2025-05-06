# Creating the Employee class
class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
    
    # Method to display employee details
    def display(self):
        print(f"Employee Name: {self.name}, Position: {self.position}")

# Creating the Department class
class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []  # List to store employee objects

    # Method to add an employee to the department
    def add_employee(self, employee):
        self.employees.append(employee)

    # Method to display department details and its employees
    def display_department(self):
        print(f"Department: {self.department_name}")
        for emp in self.employees:
            emp.display()

# Creating Employee objects
employee1 = Employee("Alice", "Manager")
employee2 = Employee("Bob", "Engineer")

# Creating a Department object
department = Department("Engineering")

# Adding employees to the department (aggregation)
department.add_employee(employee1)
department.add_employee(employee2)

# Displaying department and its employees
department.display_department()
