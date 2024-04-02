"""
Parameters vs. Arguments

Parameters are variables in a function definition, while arguments are the actual values passed to the function during its invocation.

Positional, Keyword, and Mixed Argument Passing

Arguments can be passed to functions either positionally, by keyword, or a combination of both.

Default Parameter Values

Default parameter values are values assigned to parameters in a function definition, which are used when the caller does not provide a corresponding argument.
"""

# Example demonstrating parameters vs. arguments, positional, keyword, and mixed argument passing, and default parameter values
def example_function(x, y, z=0):
    """
    Example function to demonstrate parameters, arguments, and default parameter values.
    """
    print("x:", x)
    print("y:", y)
    print("z:", z)
    print()

# Positional argument passing
print("Positional argument passing:")
example_function(1, 2)
# Output:
# x: 1
# y: 2
# z: 0

# Keyword argument passing
print("Keyword argument passing:")
example_function(y=2, x=1)
# Output:
# x: 1
# y: 2
# z: 0

# Mixed argument passing
print("Mixed argument passing:")
example_function(1, z=3, y=2)
# Output:
# x: 1
# y: 2
# z: 3

# Default parameter values
print("Default parameter values:")
example_function(1, 2, 3)
# Output:
# x: 1
# y: 2
# z: 3


# In this example:

# example_function demonstrates the concepts mentioned:
# It defines parameters x, y, and z, with z having a default value of 0.
# It prints the values of x, y, and z.
# We invoke example_function multiple times with different argument passing styles:
# Positional argument passing: Arguments are passed based on the order of parameters.
# Keyword argument passing: Arguments are passed with their corresponding parameter names.
# Mixed argument passing: Arguments are passed both positionally and by keyword.
# The output demonstrates how the function behaves with different argument passing styles and how default parameter values are used.