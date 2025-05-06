# Creating the Product class
class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price  # Private attribute

    # @property decorator to get the price
    @property
    def price(self):
        return self._price

    # @price.setter decorator to set the price
    @price.setter
    def price(self, value):
        if value < 0:
            print("Price cannot be negative!")
        else:
            self._price = value

    # @price.deleter decorator to delete the price
    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price

# Creating an object of Product class
product = Product("Laptop", 1000)

# Accessing the price using the @property getter
print(f"Initial Price: ${product.price}")

# Updating the price using the @price.setter
product.price = 1200
print(f"Updated Price: ${product.price}")

# Trying to set a negative price
product.price = -500  # This will trigger the validation in the setter

# Deleting the price using the @price.deleter
del product.price

# Trying to access the price after deletion (will raise an error)
# print(product.price)  # This will give an error since price has been deleted
