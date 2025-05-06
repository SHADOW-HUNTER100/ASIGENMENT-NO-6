# Creating a class called TemperatureConverter
class TemperatureConverter:
    # Static method to convert Celsius to Fahrenheit
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

# Calling the static method directly from the class
celsius = 25
fahrenheit = TemperatureConverter.celsius_to_fahrenheit(celsius)

# Displaying the result
print(f"{celsius}°C is equal to {fahrenheit}°F")
