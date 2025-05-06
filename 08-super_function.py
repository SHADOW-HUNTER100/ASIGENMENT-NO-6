# Creating the base class Person
class Person:
    # Constructor to set the name
    def __init__(self, name):
        self.name = name

    # Method to display the name
    def display(self):
        print("Name:", self.name)

# Creating the derived class Teacher that inherits from Person
class Teacher(Person):
    # Constructor to set the name and subject
    def __init__(self, name, subject):
        # Calling the base class constructor using super()
        super().__init__(name)
        self.subject = subject

    # Method to display teacher details
    def display(self):
        super().display()  # Call the base class display method
        print("Subject:", self.subject)

# Creating an object of the Teacher class
teacher1 = Teacher("kashif", "Mathematics")

# Displaying teacher details
teacher1.display()
