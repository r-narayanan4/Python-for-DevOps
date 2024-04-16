# sys module

# The sys module is used to work with the Python runtime environment. This means that while running your Python script, if you want to interact with your Python interpreter, then this module is helpful.

# "sys" stands for "system," but it doesn't refer to the operating system. Instead, it pertains to the Python runtime environment on your system.

# Introduction to sys module:

# The sys module provides functions and variables used to manipulate different parts of the Python runtime environment.

# How to use sys module?

# import sys

# How to get help on sys module?

# Use dir() and help() functions to get information about the sys module.
# dir(sys)
# help(sys)

import sys
"""
# Print Python interpreter version
print(sys.version)

# Print version information as a tuple
print(sys.version_info)

# Print a dictionary of loaded modules
print(sys.modules)

# Print the platform identifier
print(sys.platform)

# Print a list of directories in the Python module search path
print(sys.path)  # sys.path is an environment variable in Python
"""


# sys.argv of sys module (sys.arguments)

# sys.argv returns a list of command line arguments passed to a Python script.

# What are command line arguments?

# Let's take an example file hello.py:

# print("hello")

# If I want to run this file, I would go to the command line and run it like this:
# python hello.py

# It will print "hello".

# What if I run:
# python hello.py hi hello rln 35 3 23

# Like this, it will also print "hello" without any errors.

# So, whatever you pass after the script name (hello.py) are called command line arguments for your script. 
# While running your script, you're passing some values, and these are called command line arguments.

# So, you are passing command line arguments. If you want to print those command line arguments in the output, you need to use sys.argv.
"""
import sys

# Print the list of command line arguments
print(sys.argv)
"""
# Whatever values you give, they are taken as strings in the command line arguments, and the first value of command line arguments is your script name.

import sys


# usr_str=input("Enter your strings: ")
# usr_action=input("Enter you action on your string (valid actions are: lover.upper.title): ")
print(f"The number of command line arguments: {len(sys.argv)}")


if len(sys.argv) != 3:
    print("Usage:")
    print(f'{sys.argv[0]} <your_req_string> <lower/upper/title>')
    sys.exit()

usr_str= sys.argv[1]
usr_action=sys.argv[2]

print(f"You entered string is: {usr_str} and your actions is: {usr_action} ")

if usr_action=="lower":

    print(usr_str.lower())

elif usr_action=="upper":

    print(usr_str.upper())

elif usr_action=="title":
    
    print(usr_str.title())

else:
    print("Your option is invalid. Please select valid option from this list: lower/upper/title")

