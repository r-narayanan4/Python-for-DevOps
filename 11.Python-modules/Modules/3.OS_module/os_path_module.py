"""
The os.path module is a submodule of the os module in Python.

It provides functions for working with file and directory paths in a platform-independent manner.

Some common functionalities provided by the os.path module include:

1. Joining path components using os.path.join(): This function joins one or more path components intelligently, handling different path separators used by different operating systems.

2. Checking path existence using os.path.exists(): This function checks whether a given path exists in the filesystem.

3. Getting the basename of a path using os.path.basename(): This function returns the final component of a pathname.

4. Getting the directory name of a path using os.path.dirname(): This function returns the directory component of a pathname.

5. Splitting a path into its components using os.path.split(): This function splits a path into its directory and file components.

6. Checking whether a path is a directory using os.path.isdir(): This function checks whether a given path is a directory.

7. Checking whether a path is a file using os.path.isfile(): This function checks whether a given path is a regular file.

8. Getting the size of a file using os.path.getsize(): This function returns the size, in bytes, of a file.

9. Normalizing a path using os.path.normpath(): This function normalizes a path, eliminating double slashes and resolving references to parent directories.

10. Checking whether a path is an absolute path using os.path.isabs(): This function checks whether a given path is an absolute path.

Using the functionalities provided by the os.path module, you can perform various path-related operations in a cross-platform manner, ensuring your code works correctly on different operating systems.
"""


import os

# Example 1: Joining path components
path1 = os.path.join("usr", "local", "bin", "python")
print("Joined Path:", path1)

path = "/home/rln/module/11.Python-modules/Modules/3.OS_module/os_path_module.py"
# Example 2: Checking path existence
if os.path.exists(path):
    print("Path exists:", path)
else:
    print("Path does not exist:", path)

# Example 3: Getting the basename of a path
basename = os.path.basename(path)
print("Basename of the path:", basename)

# Example 4: Getting the directory name of a path
dirname = os.path.dirname(path)
print("Directory name of the path:", dirname)

# Example 5: Splitting a path into its components
dirpath, filename = os.path.split(path)
print("Directory path:", dirpath)
print("Filename:", filename)

# Example 6: Checking whether a path is a directory
if os.path.isdir(dirname):
    print("The path is a directory:", dirname)
else:
    print("The path is not a directory:", dirname)

# Example 7: Checking whether a path is a file
if os.path.isfile(path):
    print("The path is a file:", path)
else:
    print("The path is not a file:", path)

# Example 8: Getting the size of a file
if os.path.isfile(path):
    size = os.path.getsize(path)
    print("Size of the file:", size, "bytes")
else:
    print("The path is not a file:", path)

# Example 9: Normalizing a path
normalized_path = os.path.normpath("/usr/local/../bin/python")
print("Normalized Path:", normalized_path)

# Example 10: Checking whether a path is an absolute path
if os.path.isabs(path):
    print("The path is an absolute path:", path)
else:
    print("The path is not an absolute path:", path)

# Example 11: Checking whether a path is a symbolic link
link_path = "/usr/bin/python3"  # Example symbolic link path
if os.path.islink(link_path):
    print("The path is a symbolic link:", link_path)
    # If you want to get the target of the symbolic link, you can use os.readlink()
    target_path = os.readlink(link_path)
    print("Target of the symbolic link:", target_path)
else:
    print("The path is not a symbolic link:", link_path)


"""
Meanings of "Normalized Path" and "Absolute Path":

1. Normalized Path:
   - A normalized path is a standardized form of a file path where unnecessary elements, such as `.` (current directory) and `..` (parent directory), are removed.
   - It simplifies the path to its canonical form, making it easier to compare and work with.
   - For example, consider the path "/usr/local/../bin/python". After normalization, it becomes "/usr/bin/python", as the ".." is removed.

2. Absolute Path:
   - An absolute path is a path that uniquely identifies the location of a file or directory from the root of the file system.
   - It starts from the root directory ("/" in Unix-like systems) and specifies the complete directory structure necessary to locate the file or directory.
   - Absolute paths always begin with the root directory and do not depend on the current working directory.
   - For example, "/usr/bin/python" is an absolute path because it specifies the complete path from the root directory to the "python" executable.
"""
"""
Symbolic Link (Soft Link) and Hard Link:

1. Symbolic Link:
   - A symbolic link, also known as a soft link, is a special type of file that points to another file or directory.
   - It acts as a shortcut or alias to the target file or directory.
   - Symbolic links can span across different file systems and even point to non-existent targets.
   - They are created using the `ln -s` command in Unix-like systems or with the `os.symlink()` function in Python.
   - Symbolic links are represented by a small file that contains the path to the target.

2. Hard Link:
   - A hard link is another name for an existing file or directory. 
   - It points directly to the inode of the target file or directory on the file system.
   - Hard links cannot span across different file systems, and they cannot point to directories.
   - They are created using the `ln` command in Unix-like systems or with the `os.link()` function in Python.
   - Deleting a hard link does not delete the original file or directory as long as other hard links to it exist.
   - Changes made to the original file or directory are reflected in all hard links pointing to it.
"""
