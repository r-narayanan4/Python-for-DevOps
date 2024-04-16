# Operating System Module (os module)

# The os module is essential for automating tasks on the server-side. It allows interaction with the operating system to perform various tasks such as creating directories, removing directories, identifying the current directory, and more.

# To gain confidence in using the os module, we can divide it into four main parts:

# 1. Operations of the os module
# This part involves understanding the general operations and functionalities provided by the os module. It includes methods for executing commands, managing processes, and working with files and directories.

# 2. OS module (os)
# The core part of the os module provides functions for interacting with the operating system. It offers a wide range of methods to perform tasks like file and directory manipulation, process management, environment variables manipulation, and more.

# 3. os.path module (os.path)
# The os.path submodule provides functions for path manipulation and file system operations. It offers methods for joining and splitting paths, checking file existence, retrieving file properties, and navigating the file system structure.

# 4. os.system() function
# The os.system() function is a simple way to execute shell commands from within a Python script. It allows running arbitrary shell commands as if they were typed on the command line. However, it is recommended to use more robust alternatives like the subprocess module for better control and security.

# 5. os.walk() function
# The os.walk() function is a powerful tool for traversing directory trees and performing operations on files and directories within them. It generates a tuple of (root, dirs, files) for each directory in the tree, allowing recursive traversal and manipulation of the directory structure.

# To Practise run the logic one by one commenting

import os

# # Getting the separator used in the current operating system
# separator = os.sep
# print("Separator:", separator)

# # Getting the current working directory
# current_dir = os.getcwd()
# print("Current Directory:", current_dir)

# # Changing the current working directory to a specified path
# new_dir = "/home/rln/module/11.Python-modules/Modules/"
# os.chdir(new_dir)
# print("Changed Directory to:", os.getcwd())

# # Listing files and directories in a specified path
# files_and_dirs = os.listdir(os.getcwd())
# print("Files and Directories in current directory:", files_and_dirs)

# # Creating a new directory
# new_directory = "new_directory"
# os.mkdir(new_directory)
# print("New directory created:", new_directory)

# # Creating directories recursively
# new_nested_directory = os.path.join("new_parent_directory", "new_child_directory") #os.path.join() is a function provided by the os.path module in Python. It's used to concatenate multiple path components into a single path, using the appropriate separator for the current operating system.
# os.makedirs(new_nested_directory)
# print("New nested directories created:", new_nested_directory)

# # Removing a file
# file_to_remove = "/home/rln/module/11.Python-modules/Modules/3.OS_module/new_parent_directory/new.txt"
# open(file_to_remove, 'w').close()  # Creating a file for demonstration
# os.remove(file_to_remove)
# print("File removed:", file_to_remove)

# # Removing directories recursively
# dir_to_remove = "directory_to_remove"
# os.mkdir(dir_to_remove)  # Creating a directory for demonstration
# os.removedirs(dir_to_remove)
# print("Directory removed recursively:", dir_to_remove)

# # Removing an empty directory
# empty_dir_to_remove = "empty_directory_to_remove"
# os.mkdir(empty_dir_to_remove)  # Creating a directory for demonstration
# os.rmdir(empty_dir_to_remove)
# print("Empty directory removed:", empty_dir_to_remove)

# # Renaming a file or directory
# old_name = "old_name.txt"
# new_name = "new_name.txt"
# open(old_name, 'w').close()  # Creating a file for demonstration
# os.rename(old_name, new_name)
# print("File renamed from", old_name, "to", new_name)

# # Getting environment variables
# environment_variables = os.environ
# print("Environment Variables:", environment_variables)

# Getting the user ID of the current process

user_id = os.getuid()
print("User ID of current process:", user_id)

# Getting the process ID of the current process
process_id = os.getpid()
print("Process ID of current process:", process_id)




