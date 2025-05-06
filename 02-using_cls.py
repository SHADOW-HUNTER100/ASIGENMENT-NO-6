# Creating a class called Counter
class Counter:
    # Class variable to keep count of objects
    count = 0

    # Constructor to update count when object is created
    def __init__(self):
        Counter.count += 1

    # Class method to display the number of objects
    @classmethod
    def show_count(cls):
        print("Total objects created:", cls.count)

# Creating some objects
obj1 = Counter()
obj2 = Counter()
obj3 = Counter()

# Calling class method to display count
Counter.show_count()
