# Python Modules

## Module in Python

A module in Python is a file containing Python definitions and statements, such as functions, classes, and variables, which can be reused in other Python scripts or programs.

## Use of Module

Modules promote code reusability by allowing developers to encapsulate code into separate files, making it easier to manage and maintain large codebases.

## Types of Python Module

1. **Default Module**: These are built-in modules that come with the Python installation.
2. **Third-Party Module**: These are modules developed by external sources and can be installed using package managers like pip.

## Example for Default Module

```python
import math

print(math.sqrt(25))  # Output: 5.0
```

## Example for Third-Party Module

```bash
pip install requests
```

## Using dir() to Get Methods of a Module

```python

import math

print(dir(math))
```

## Using help() to Get Help on Using a Module

```python
import math

help(math)
```

## Difference Between import and from

1. **import:** Imports the entire module. To use any function or variable from the module, you need to prefix it with the module name.

```python

import math
print(math.sqrt(25))  # Output: 5.0
```

1. **from:** Imports specific functions or variables from the module. You can directly use the imported functions or variables without prefixing them with the module name.

```python

from math import sqrt
print(sqrt(25))  # Output: 5.0
```

## Some other Example for Importing

```Python

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

```
