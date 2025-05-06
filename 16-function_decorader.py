# Creating the decorator function
def log_function_call(func):
    # This is the wrapper function that adds logging before the actual function call
    def wrapper():
        print("Function is being called")
        return func()  # Calling the original function
    return wrapper  # Returning the wrapper function

# Creating the function say_hello
@log_function_call  # Applying the decorator to say_hello
def say_hello():
    print("Hello, World!")

# Calling the decorated function
say_hello()
