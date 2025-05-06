# Creating a class called Student
class Student:
    # Constructor to initialize name and marks
    def __init__(self, name, marks):
        self.name = name  # 'self' refers to the current object
        self.marks = marks

    # Method to display student details
    def display(self):
        print("Student Name:", self.name)
        print("Marks:", self.marks)

# Creating an object of the Student class
student1 = Student("Alice", 92)

# Calling the display method
student1.display()
