# Creating a class called MathUtils
class MathUtils:
    # Static method to add two numbers
    @staticmethod
    def add(a, b):
        return a + b

# Calling the static method directly from the class
result = MathUtils.add(10, 5)

# Displaying the result
print("Sum:", result)
