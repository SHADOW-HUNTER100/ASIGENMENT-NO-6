# Creating the Countdown class
class Countdown:
    def __init__(self, start):
        self.start = start  # Initialize with the start number

    # __iter__ method to return the iterator (itself in this case)
    def __iter__(self):
        self.current = self.start  # Set the current number to the start
        return self  # Return the iterator object itself

    # __next__ method to return the next value in the countdown
    def __next__(self):
        if self.current <= 0:  # If countdown reaches 0, stop iteration
            raise StopIteration
        self.current -= 1  # Decrement the current value
        return self.current  # Return the current value

# Creating an object of Countdown with a starting number
countdown = Countdown(5)

# Using the Countdown object in a for-loop (iterating through the countdown)
for number in countdown:
    print(number)
