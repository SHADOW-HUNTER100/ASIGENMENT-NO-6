# Creating the Multiplier class
class Multiplier:
    def __init__(self, factor):
        self.factor = factor  # Initialize with the factor to multiply

    # __call__ method to make the object callable
    def __call__(self, number):
        return number * self.factor

# Creating an object of Multiplier class with a factor of 5
multiplier = Multiplier(5)

# Using callable() to check if the object is callable
print(f"Is multiplier callable? {callable(multiplier)}")  # Should return True

# Calling the object like a function
result = multiplier(10)  # This will call the __call__ method
print(f"Multiplying 10 by the factor: {result}")
