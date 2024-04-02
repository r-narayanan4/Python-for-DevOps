# This script demonstrates defining functions, calling functions, and different forms of functions.

# Function with no parameters
def greet():
    """This function greets the user."""
    print("Hello! Welcome to the world of functions.")

# Function with parameters
def greet_with_name(name):
    """This function greets the user with their name."""
    print("Hello,", name + "! Welcome to the world of functions.")

# Function with default parameter value
def greet_with_default(name="there"):
    """This function greets the user with a default name."""
    print("Hello,", name + "! Welcome to the world of functions.")

# Call the functions with different forms
print("Calling functions:")
greet()  # Calling function with no parameters
greet_with_name("Alice")  # Calling function with one parameter
greet_with_default()  # Calling function with default parameter value


# Output

'''
Calling functions:
Hello! Welcome to the world of functions.
Hello, Alice! Welcome to the world of functions.
Hello, there! Welcome to the world of functions.
'''