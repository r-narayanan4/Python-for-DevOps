"""
The raise statement in Python is used to explicitly raise an exception within your code. 
When you encounter an exceptional condition that you want to handle, you can use raise to create and raise an exception object. 
This allows you to indicate that something unexpected has happened during the execution of your program.
"""


# Function to calculate square root
def calculate_square_root(number):
    """
    Function to calculate the square root of a number.

    Args:
        number (float): The number to calculate the square root of.

    Returns:
        float: The square root of the number.
    """
    if number < 0:
        raise ValueError("Error: Negative number not allowed")
    return number ** 0.5

# Example usage
try:
    # Asking user for input
    num = float(input("Enter a number: "))

    # Calculating square root
    result = calculate_square_root(num)
    print("Square root:", result)

except ValueError as ve:
    # Handling the custom exception
    print(ve)

except:
    # Handling other exceptions
    print("Error: An unexpected error occurred.")
