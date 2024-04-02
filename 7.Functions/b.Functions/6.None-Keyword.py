"""
The None Keyword

None is a special constant in Python that represents the absence of a value or a null value.
"""

# Example demonstrating the usage of the None keyword
def check_value(value):
    """
    Function to check if a value is None.
    """
    if value is None:
        print("The value is None.")
    else:
        print("The value is not None.")

# Testing the function with different values
check_value(None)           # Output: The value is None.
check_value(5)              # Output: The value is not None.
check_value("Hello")        # Output: The value is not None.
check_value([])             # Output: The value is not None.

