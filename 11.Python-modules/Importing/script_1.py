# Define a function to add two numbers
def add(a, b):
    # Print the result of the addition
    print(f"The addition of {a} and {b} is {a + b}")

# Define a function to subtract two numbers
def sub(a, b):
    # Print the result of the subtraction
    print(f"The subtraction of {a} and {b} is {a - b}")

# Define the main function
def main():
    # Assign values to variables
    x = 8
    y = 2

    # Call the add function with x and y as arguments
    add(x, y)
    
    # Call the sub function with x and y as arguments
    sub(x, y)

# Check if the script is being run directly
if __name__ == "__main__":
    # If so, execute the main function
    main()
    
# Print a message indicating that this code block belongs to script_2.py
print(f"This is from script_2.py:", __name__)



'''

f-strings in Python provide a concise, readable, and efficient way to create formatted strings by allowing you to embed expressions, variables, and function calls directly within string literals.

'''

'''
The if __name__ == "__main__": construct is commonly used in Python scripts to ensure that certain code blocks are only executed when the script is run directly, as opposed to being imported as a module into another script.

'''