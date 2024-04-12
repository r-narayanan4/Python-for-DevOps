# Printing welcome message
print("Welcome to exceptions concept")

# Printing a message
print("Now it is fine")

# Opening a file named "nari.txt"
# This will raise a FileNotFoundError since the file doesn't exist
'''
fo=open("nari.txt")
'''

# Exception handling using a try-except block
'''
try:
    # Attempting to open the file "nari.txt"
    fo = open("nari.txt")
    # Printing the content of the file
    print(fo.read())
    # Closing the file
    fo.close()
# Handling exceptions
except Exception as e:
    # Printing the exception message
    print(e)
'''

# A list containing elements
my_list = [3, 4, 5]

# Accessing an element at an index that doesn't exist
# This will raise an IndexError
'''
try:
    print(my_list[4])
except Exception as e:
    print(e)
'''

# This code will also execute after the exception handling block

# Attempting to access an element in the list at an index that doesn't exist
# This will raise an IndexError and terminate the program
# print(my_list[4])

# This line of code will not execute due to the raised exception above

# Attempting to import a module that doesn't exist
# This will raise an ImportError since the module "fabric" doesn't exist
try:
    import fabric
except Exception as e:
    # Printing the exception message
    print(e)
