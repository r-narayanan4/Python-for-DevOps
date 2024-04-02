"""
Concepts:
1. Positional Arguments:
   Positional arguments are values passed to a function in a specific order, where each value corresponds to a parameter in the function definition.

2. Keyword Arguments:
   Keyword arguments are values passed to a function with the associated parameter name, allowing you to specify arguments out of order.

3. Default Arguments:
   Default arguments are parameters in a function that have preset values, which are used if the caller does not provide a corresponding argument.
"""

# Function with positional arguments
def greet_with_positional(name, greeting):
    """This function greets the user using positional arguments."""
    print(f"{greeting}, {name}!")

# Function with keyword arguments
def greet_with_keywords(name, greeting="Hello"):
    """This function greets the user using keyword arguments."""
    print(f"{greeting}, {name}!")

# Function with default arguments
def greet_with_defaults(name="there", greeting="Hello"):
    """This function greets the user using default arguments."""
    print(f"{greeting}, {name}!")

# Demonstrate positional arguments
print("Using positional arguments:")
greet_with_positional("Alice", "Hi")  # Positional arguments passed in order
greet_with_positional("Bob", "Howdy")  # Positional arguments passed in order

# Demonstrate keyword arguments
print("\nUsing keyword arguments:")
greet_with_keywords(name="Charlie")  # Using default greeting
greet_with_keywords(name="David", greeting="Hey") # Providing both name and greeting

# Demonstrate default arguments
print("\nUsing default arguments:")
greet_with_defaults()  # Using default name and greeting
greet_with_defaults("Eve")  # Providing only name
greet_with_defaults(greeting="Hola")  # Providing only greeting

# Output

'''
Using positional arguments:
Hi, Alice!
Howdy, Bob!

Using keyword arguments:
Hello, Charlie!
Hey, David!

Using default arguments:
Hello, there!
Hello, Eve!
Hola, there!

'''

"""
Difference Between Keyword Arguments and Default Arguments:

Keyword Arguments:
- Keyword arguments are values passed to a function with the associated parameter name.
- They allow you to specify arguments out of order by explicitly providing the parameter name.
- Keyword arguments offer flexibility in function calls as you can provide values for specific parameters regardless of their position.
- They are particularly useful when you want to skip some arguments and only provide values for certain parameters.
- Example: greet_with_keywords(name="Charlie", greeting="Hey")

Default Arguments:
- Default arguments are parameters in a function that have preset values.
- If the caller does not provide a corresponding argument for these parameters, the default values are used instead.
- Default arguments provide a fallback value for parameters if no value is provided during the function call.
- They are useful for defining optional parameters or parameters with commonly used values.
- Example: def greet_with_defaults(name="there", greeting="Hello")
"""
