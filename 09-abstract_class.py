from abc import ABC, abstractmethod

# Creating an abstract class Shape
class Shape(ABC):
    # Abstract method to calculate area
    @abstractmethod
    def area(self):
        pass

# Creating a derived class Rectangle that implements area
class Rectangle(Shape):
    # Constructor to set the length and width
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Implementing the abstract method area
    def area(self):
        return self.length * self.width

# Creating an object of Rectangle class
rect = Rectangle(5, 3)

# Displaying the area
print("Area of Rectangle:", rect.area())
