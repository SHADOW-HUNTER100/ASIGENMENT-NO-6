# Creating the class decorator add_greeting
def add_greeting(cls):
    # Adding a greet() method to the class dynamically
    def greet(self):
        return "Hello from Decorator!"
    
    # Attaching the greet method to the class
    cls.greet = greet
    return cls  # Returning the modified class

# Applying the class decorator to the Person class
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"My name is {self.name}")

# Creating an object of the Person class
person = Person("Alice")

# Calling the greet() method added by the decorator
print(person.greet())  # Output: Hello from Decorator!
