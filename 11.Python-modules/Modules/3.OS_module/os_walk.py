"""
os.walk() Method:

The os.walk() method is a powerful tool provided by the os module in Python. It allows you to traverse directory trees, iterating over the directories, subdirectories, and files within a specified directory.

Functionality:
- os.walk() generates the file names, directory names, and root directory for each directory in the directory tree.
- It starts at the top-level directory specified as its argument and traverses recursively through all its subdirectories.
- For each directory in the directory tree, os.walk() yields a tuple containing three elements:
    - The current directory path (string)
    - A list of subdirectory names within the current directory (list of strings)
    - A list of file names within the current directory (list of strings)
- os.walk() uses a depth-first search algorithm to traverse the directory tree, visiting all subdirectories before moving to the next level.

Usage:
- You typically use os.walk() when you need to perform operations on every file or directory within a directory tree, such as searching for specific files, processing files, or copying directory structures.
- It's commonly used in tasks like file system navigation, file manipulation, backup operations, and batch processing.
"""
# Example:

import os

# Traverse the directory tree starting from the current directory
for root, dirs, files in os.walk('/home/rln/module/11.Python-modules/Modules'):
    print("Current Directory:", root)
    print("Subdirectories:", dirs)
    print("Files:", files)
    print()




# import os

# path="/home/rln/module/11.Python-modules/Modules/"
# #print(list(os.walk(path)))
# print("-------------")
# for r,d,f in os.walk(path):
#     if len(f) !=0:
#         print(r)
#         for each_file in f:
#             print(os.path.join(r,each_file))
#             print("-------------")
