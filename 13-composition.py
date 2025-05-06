# Creating the Engine class
class Engine:
    def __init__(self, type_of_engine):
        self.type_of_engine = type_of_engine
    
    # Method to start the engine
    def start(self):
        print(f"The {self.type_of_engine} engine is now running.")

# Creating the Car class
class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine  # Engine object is passed during initialization
    
    # Method to start the car (which internally starts the engine)
    def start_car(self):
        print(f"The {self.brand} car is starting...")
        self.engine.start()  # Accessing the Engine's start method

# Creating an Engine object
engine1 = Engine("V8")

# Creating a Car object and passing the Engine object to it
car1 = Car("Ford Mustang", engine1)

# Starting the car (which will start the engine)
car1.start_car()
