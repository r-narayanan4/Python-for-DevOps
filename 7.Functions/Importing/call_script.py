# call_scripts.py

# Importing functions from script_1.py and script_2.py
import script_1
import script_2

# Define a main function to call functions from script_1.py and script_2.py
def main():
    x = 8
    y = 2
    
    # Call add function from script_1.py
    script_1.add(x, y)
    
    # Call sub function from script_1.py
    script_1.sub(x, y)
    
    # Call mul function from script_2.py
    script_2.mul(x, y)
    
    # Call div function from script_2.py
    script_2.div(x, y)

# Check if this script is being run directly
if __name__ == "__main__":
    # If so, call the main function
    main()
