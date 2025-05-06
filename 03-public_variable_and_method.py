# Creating a class called Car
class Car:
    # Public variable
    brand = "Toyota"

    # Public method
    def start(self):
        print(self.brand, "car has started.")

# Creating an object of the Car class
my_car = Car()

# Accessing public variable from outside the class
print("Car brand:", my_car.brand)

# Accessing public method from outside the class
my_car.start()
