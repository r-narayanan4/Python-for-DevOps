# script_2.py

# Importing functions from script_1.py
import script_1

# Define a function to perform multiplication
def mul(a, b):
    print(f"The multiplication of {a} and {b} is {a * b}")

# Define a function to perform division
def div(a, b):
    print(f"The division of {a} and {b} is {a / b}")

# Define a main function
def main():
    x = 8
    y = 2
    
    # Call add function from script_1.py
    script_1.add(x, y)
    
    # Call sub function from script_1.py
    script_1.sub(x, y)
    
    # Call mul function defined in this script
    mul(x, y)
    
    # Call div function defined in this script
    div(x, y)

# Check if this script is being run directly
if __name__ == "__main__":
    # If so, call the main function
    main()

# Print a message indicating that this is from script_2.py
print(f"This is from script_2.py: {__name__}")
