import sys  # Import the sys module to access command-line arguments

# Define a function to print each argument
def echo_arguments(args):
    for arg in args:  # Loop through each argument in the list
        print(arg)    # Print the argument

if __name__ == "__main__":  # Check if the script is being run directly
    # Get command-line arguments excluding the script name
    arguments = sys.argv[1:]  # Get command-line arguments
    echo_arguments(arguments)  # Call the function to print arguments

"""
import sys: This line tells Python to import the sys module, which provides access to some variables and functions related to the Python interpreter and system.

def echo_arguments(args):: Here, we're defining a function named echo_arguments that takes one parameter, args, which is expected to be a list.

for arg in args:: This line starts a loop that iterates through each item in the args list.

print(arg): Inside the loop, this line prints each item (arg) in the args list.

if __name__ == "__main__":: This line checks if the script is being run directly by the Python interpreter (as opposed to being imported into another script).

arguments = sys.argv[1:]: Here, we're capturing the command-line arguments passed to the script. sys.argv is a list that contains the script name and any command-line arguments passed to it. We slice it ([1:]) to exclude the script name and store the rest of the arguments in the arguments variable.

echo_arguments(arguments): This line calls the echo_arguments function we defined earlier, passing in the list of command-line arguments as its argument.

So, in simpler terms, this program prints out all the command-line arguments that are provided to it when it is run.
"""