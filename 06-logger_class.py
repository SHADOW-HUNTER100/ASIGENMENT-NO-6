# Creating a class called Logger
class Logger:
    # Constructor - prints when the object is created
    def __init__(self):
        print("Logger object created.")

    # Destructor - prints when the object is destroyed
    def __del__(self):
        print("Logger object destroyed.")

# Creating an object of Logger class
log1 = Logger()

# Optionally deleting the object to trigger the destructor
del log1
