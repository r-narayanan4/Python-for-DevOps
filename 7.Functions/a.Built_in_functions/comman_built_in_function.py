# Using built-in functions in DevOps Python scripting

# 1. range(): Generates a sequence of numbers within a specified range.
numbers = list(range(1, 6))
print("Generated sequence of numbers:", numbers)

# Output:
# Generated sequence of numbers: [1, 2, 3, 4, 5]

# 2. int(): Converts a given value to an integer.
value_int = int("10")
print("Converted value to integer:", value_int)

# Output:
# Converted value to integer: 10

# 3. float(): Converts a given value to a floating-point number.
value_float = float("3.14")
print("Converted value to float:", value_float)

# Output:
# Converted value to float: 3.14

# 4. str(): Converts a given value to a string.
value_str = str(123)
print("Converted value to string:", value_str)

# Output:
# Converted value to string: 123

# 5. id(): Returns the identity (unique identifier) of an object.
identity = id("hello")
print("Identity of the object:", identity)

# Output:
# Identity of the object: 140265159424304

# 6. type(): Returns the type of an object.
data_type = type(10)
print("Type of the object:", data_type)

# Output:
# Type of the object: <class 'int'>

# 7. None: Represents the absence of a value.
value = None
print("Value assigned as None:", value)

# Output:
# Value assigned as None: None

# 8. len(): Returns the length of an object.
length = len([1, 2, 3, 4, 5])
print("Length of the object:", length)

# Output:
# Length of the object: 5

'''In the context of the Python built-in function id(), "identity" refers to the unique identifier of an object. Every object in Python has a unique identifier associated with it. This identifier remains constant throughout the object's lifetime and is guaranteed to be unique among simultaneously existing objects.

The id() function returns this unique identifier, which is typically represented as an integer. It allows you to distinguish one object from another, even if they have the same value.

For example, consider the following:

a = "hello"
b = "hello"
print(id(a))  # Output: 140360299494576
print(id(b))  # Output: 140360299494576

'''

"""
Concept Explanation:

9. dir():
   - Purpose: Returns a sorted list of valid attributes and methods associated with an object.
   - Usage: dir(object)
   - Real-time Example: 
     Suppose you're working with a Python module 'math' and you're unsure about the available functions. 
     By using dir(math), you can quickly explore all the functions and constants provided by the math module.

"""

# Real-time Example Program:

# Suppose you're working with the 'math' module and want to explore its available functions.
import math

# Use dir() to see all the available attributes and methods in the math module
print("Attributes and methods of the math module:")
print(dir(math))

# Attributes and methods of the math module:
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']

"""
Concept Explanation:

10. __str__():
    - Purpose: Returns the string representation of an object when str() is called on it or when it's printed.
    - Usage: object.__str__()
    - Real-time Example:
      Consider a class 'Product' representing products in an inventory system. 
      Implementing __str__() in the Product class allows you to define how Product objects are printed, 
      making it easier to display product information in a human-readable format.

Explanation of the Concept:

__str__() is a special method in Python that allows objects to define how they should be represented as strings.
When the str() function is called on an object or when the object is printed, Python internally calls the __str__() method of that object.
This method must return a string, and it's commonly used to provide a human-readable representation of the object's state
"""

# Real-time Example Program:

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __str__(self):
        return f"{self.name} - ${self.price}"

# Create a Product object
product1 = Product("Laptop", 1200)

# Print the string representation of the Product object
print("String representation of the Product object:")
print(str(product1))

# output

# String representation of the Product object:
# Laptop - $1200

"""
Concept Explanation:

11. __name__:
    - Purpose: Stores the name of the current module.
    - Usage: __name__
    - Real-time Example:
      Suppose you have a module 'utils.py' containing various utility functions. 
      By checking __name__ == '__main__', you can include code that should only run when the script is executed directly. 
      This allows you to have testing or debugging code that doesn't run when the module is imported into another script.
Explanation of the Concept:

__name__ is a special built-in variable in Python that stores the name of the current module.
When a Python script is run directly, the value of __name__ is set to '__main__'.
When a Python script is imported as a module into another script, the value of __name__ is set to the name of the module.
Now, let's provide an example program along with its output demonstrating the usage of __name__:
"""
# Real-time Example Program:

# Suppose you have a Python module 'utils.py' containing various utility functions.

# Utility function to add two numbers
def add(a, b):
    return a + b

# Check if the script is run directly
if __name__ == "__main__":
    # This code block will only run if the script is executed directly.
    # It could contain testing or debugging code.
    print("Running some tests...")
    result = add(3, 5)
    print("Result of adding 3 and 5:", result)
    print("Tests complete.")

# Output (when running the script directly):
    
# Running some tests...
# Result of adding 3 and 5: 8
# Tests complete.
    
'''Explanation of the above Example:

We have a module named 'utils.py' containing a utility function add(a, b) to add two numbers.
By checking __name__ == "__main__", we ensure that the code block inside the if statement only runs when the script is executed directly.
This allows us to include testing or debugging code that should not run when the module is imported into another script.
'''
# How to run indirectly

'''
To run a Python script indirectly (i.e., when it's imported as a module into another script), you simply import the module using the import statement in another Python script. Here's a step-by-step guide:

Create the Module:
First, create the Python script (module) that you want to run indirectly. Let's call it utils.py for this example.


# utils.py
def add(a, b):
    return a + b

if __name__ == "__main__":
    print("This script is being run directly.")
else:
    print("This script is being imported as a module.")

Create the Main Script:
Create another Python script (main script) that will import the utils.py module. Let's call it main.py.


# main.py
import utils

result = utils.add(3, 5)
print("Result of adding 3 and 5:", result)

Run the Main Script:
Run the main.py script directly using the Python interpreter.


$ python main.py

When you run main.py, it will import the utils.py module. The code inside utils.py will be executed, but the code inside the if __name__ == "__main__": block will not run, since utils.py is being imported as a module. Instead, the else block will execute, indicating that the script is being imported as a module.


When you run the main.py script, you will see the following output:


This script is being imported as a module.
Result of adding 3 and 5: 8
Explanation of the Output:

The first line indicates that the utils.py script is being imported as a module into main.py.
The second line prints the result of adding 3 and 5, which is 8, using the add() function from the utils.py module.

In the previous example, running main.py is a direct execution of the script. To demonstrate running a script indirectly, let's modify the main.py script to import utils.py from another script.

Here's the revised main.py script:


# main.py
import another_script

result = another_script.multiply(3, 5)
print("Result of multiplying 3 and 5:", result)

And create a new script named another_script.py:


# another_script.py
def multiply(a, b):
    return a * b

if __name__ == "__main__":
    print("This script is being run directly.")
else:
    print("This script is being imported as a module.")


    
Now, when you run main.py, it will import another_script.py indirectly.

Here's the output:

This script is being imported as a module.
Result of multiplying 3 and 5: 15

Explanation:

The first line indicates that another_script.py is being imported as a module into main.py.
The second line prints the result of multiplying 3 and 5, which is 15, using the multiply() function from another_script.py.

'''
