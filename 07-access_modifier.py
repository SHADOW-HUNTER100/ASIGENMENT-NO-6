# Creating a class called Employee
class Employee:
    # Public variable
    name = "John Doe"

    # Protected variable (conventionally protected)
    _salary = 50000

    # Private variable (not accessible directly outside the class)
    __ssn = "123-45-6789"

# Creating an object of Employee class
employee1 = Employee()

# Accessing the public variable
print("Employee Name:", employee1.name)

# Accessing the protected variable
print("Employee Salary:", employee1._salary)

# Accessing the private variable directly (this will fail)
# print("Employee SSN:", employee1.__ssn)  # This will cause an AttributeError

# Accessing the private variable via name mangling
print("Employee SSN (via name mangling):", employee1._Employee__ssn)
