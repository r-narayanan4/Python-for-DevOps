# Program: Division Program with Error Handling
# Concept: Demonstrating try, except, else, and finally blocks in Python.

# Function to perform division operation
def perform_division(dividend, divisor):
    try:
        # Attempting division
        result = dividend / divisor
    except ZeroDivisionError:
        # Handling division by zero error
        print("Error: Division by zero is not allowed!")
    else:
        # Executed if no exception occurred
        print("Division successful. Result:", result)
    finally:
        # Executed regardless of exception occurrence
        print("Finally block executed, regardless of errors.")

# Example usage
if __name__ == "__main__":
    # Asking user for input
    dividend = float(input("Enter the dividend: "))
    divisor = float(input("Enter the divisor: "))
    print(f"You are dividing {dividend} by {divisor}")

    # Calling the function with user inputs
    perform_division(dividend, divisor)


# Output

# Enter the dividend: 10
# Enter the divisor: 2
# You are dividing 10.0 by 2.0
# Division successful. Result: 5.0
# Finally block executed, regardless of errors.

# Enter the dividend: 10
# Enter the divisor: 0
# You are dividing 10.0 by 0.0
# Error: Division by zero is not allowed!
# Finally block executed, regardless of errors.
