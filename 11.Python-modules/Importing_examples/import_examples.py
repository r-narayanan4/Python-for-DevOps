'''
## Import statements

Import statements are used to import modules or specific objects from modules into your Python program. 
They allow you to reuse code and organize your codebase into manageable units.

## Multiple ways of importing

Python provides multiple ways of importing modules, including importing specific objects from a module, 
importing all objects from a module, and importing modules under an alias

'''


# Importing specific objects from a module
# 1. Importing specific objects from a module:
# You can import specific objects (functions, classes, variables) from a module using the from ... import ... syntax.

from math import pi, sqrt

# Print message and use the imported objects
print("Importing specific objects from a module:")
print("Value of pi:", pi)
print("Square root of 16:", sqrt(16))
print()

# Importing all objects from a module (not recommended)
# 2. Importing all objects from a module:
# You can import all objects from a module using the import * syntax. However, this is generally 
# discouraged because it pollutes the global namespace and may lead to naming conflicts.

from math import *

# Print message and use the imported objects

print("Importing all objects from a module (not recommended):")
print("Value of pi:", pi)
print("Square root of 16:", sqrt(16))
print()

# Importing modules under an alias

# 3. Importing modules under an alias:
# You can import a module under an alias using the import ... as ... syntax. 
# This is useful when dealing with modules with long names or to avoid naming conflicts.

import math as m

# Print message and use the imported objects with alias
print("Importing modules under an alias:")
print("Value of pi:", m.pi)
print("Square root of 16:", m.sqrt(16))
print()

# Importing the entire module
# 4. Importing the entire module:
# You can import the entire module without importing specific objects using the 
# import ... syntax. This allows you to access all objects within the module using dot notation.

import math

# Print message and use the imported objects
print("Importing the entire module:")
print("Value of pi:", math.pi)
print("Square root of 16:", math.sqrt(16))
print()

# Importing modules conditionally

# 5. Importing modules conditionally:
# You can import modules conditionally using import ... inside a 
# function or conditional block. This can be useful for optimizing imports or dealing with optional dependencies.

def my_function():
    # Importing math module only inside the function
    import math
    
    # Print message and use the imported objects
    print("Importing modules conditionally inside a function:")
    print("Square root of 16:", math.sqrt(16))

# Call the function to demonstrate conditional import
my_function()
