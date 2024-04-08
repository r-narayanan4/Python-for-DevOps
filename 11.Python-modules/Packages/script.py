# example_script.py

# Importing functions from modules within the package
from my_package.module1 import hello
from my_package.sub_package.module2 import world

# Calling functions from the imported modules
hello()
world()


"""
Explanation:

script.py is the Python script that uses the my_package package.
It imports the hello() function from my_package.module1 and the world() function from my_package.subpackage.module2.
When you run example_script.py, it will execute the imported functions, printing "Hello from module1" and "World from module2" as output.
The my_package directory contains the package structure with the necessary __init__.py files and modules.
The __init__.py files are used to mark the directories as Python package directories.
module1.py and module2.py contain the code for the functions hello() and world(), respectively.

"""