"""

In Python, the concept of name scopes refers to the visibility and accessibility of variables within different parts of your code. Variables defined within certain scopes, such as within functions or classes, have different visibility rules. Understanding name scopes is crucial for avoiding conflicts and organizing your code effectively.

"""
# This is a Python example demonstrating name scopes with functions.

# Global scope:
# Variables defined outside of any function have global scope.
global_var = 10

def my_function():
    # Function scope:
    # Variables defined inside a function are accessible only within that function.
    local_var = 20
    print("Inside the function, local_var:", local_var)
    print("Inside the function, global_var:", global_var)

def another_function():
    # Another function scope:
    # Variables defined inside another function are not accessible in different functions.
    inner_var = 30
    print("Inside another_function, inner_var:", inner_var)

# Global scope:
print("Outside all scopes, global_var:", global_var)

# Function scope:
my_function()

# Attempt to access local_var outside of its scope will raise an error:
# print("Outside the function, local_var:", local_var)  # Uncomment to see the error

# Attempt to access inner_var outside of its scope will raise an error:
# print("Outside another_function, inner_var:", inner_var)  # Uncomment to see the error

# Another function scope:
another_function()


# Output:

# Outside all scopes, global_var: 10
# Inside the function, local_var: 20
# Inside the function, global_var: 10
# Inside another_function, inner_var: 30


# In this example:

# global_var is accessible everywhere because it's defined in the global scope.
# local_var is accessible only within the my_function() function where it's defined.
# inner_var is accessible only within the another_function() function where it's defined