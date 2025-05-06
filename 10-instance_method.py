# Creating a class called Dog
class Dog:
    # Constructor to initialize name and breed
    def __init__(self, name, breed):
        self.name = name  # Instance variable name
        self.breed = breed  # Instance variable breed

    # Instance method to bark
    def bark(self):
        print(f"{self.name} is barking!")

# Creating an object of the Dog class
dog1 = Dog("Buddy", "Golden Retriever")

# Calling the bark method
dog1.bark()
