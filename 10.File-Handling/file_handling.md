# Python File Handling

Python file handling is a versatile and powerful mechanism for performing operations on files. It allows users to work with different types of files and perform various operations such as creating, writing, reading, and deleting files. File handling is crucial as it enables the storage of data in files after running the program.

## Advantages of File Handling in Python

- **Versatility**: Python file handling allows users to perform a variety of operations on files like creating, writing, reading, and deleting files.
- **Flexibility**: Python file handling provides flexibility as it allows working with different types of files like binary, text, CSV Files, etc., and performing a variety of operations.
- **User-friendly**: Python provides a user-friendly, simple, and concise way for file handling.
- **Cross-platform**: Python file handling can be performed on different platforms such as Linux, Mac, Windows, etc.

## Disadvantages of File Handling in Python

- **Error-prone**: Python file handling sometimes throws errors when the code is not written properly or if there is an issue in the file system.
- **Security risks**: There is a security risk in Python file handling, especially when the input is taken from the user and it tries to modify and access sensitive files of the system.
- **Complexity**: Python file handling becomes complex while working with advanced file types and operations.
- **Performance**: File handling in Python is slower compared to file handling in other programming languages, especially when working with complex operations and large files.

## Modes of File Handling in Python

In Python, file handling modes are used to determine how a file should be opened and operated upon. Python provides several file handling modes that allow you to perform different operations on files. Here are the most commonly used file handling modes in Python:

## File Handling Modes in Python

File handling modes in Python are used to specify how a file should be opened and operated upon. Each mode serves a different purpose and allows performing specific operations on files.

## 1. Read Mode 'r'

The read mode is denoted by the character 'r' and is used when you want to open a file for reading its contents. With this mode, you cannot modify the file; it is primarily for reading data.

## 2. Write Mode 'w'

The write mode ('w') is used to write data to a file. If the file does not exist, it will be created. If it already exists, the contents will be overwritten. To append data to the existing file content, use the 'a' mode instead.

## 3. Append Mode 'a’

The append mode ('a') is used to append data to an existing file. If the file does not exist, it will be created. The new data will be added to the end of the existing file content, without overwriting it.

## 4. Binary Mode 'b’

Binary mode ('b') is used for handling binary files like images, videos, and audios. For example, 'rb' is used to read a binary file, and 'wb' is used to write to a binary file.

## 5. Exclusive Creation Mode 'x'

The exclusive creation mode ('x') is used to create a new file, but it raises a FileExistsError if the file already exists. This mode ensures that a new file is created without overwriting any existing file with the same name.

## 6. Update Mode '+'

The update mode ('+') is used to open a file for both reading and writing. It is added to other modes. For example, 'r+' is used to open a file for both reading and writing simultaneously.

To use these modes, you can pass them as the second argument when using the open() function to open a file. For example:

```python

# Open a file in read mode and then close it
file = open('example.txt', 'r')
file.close()

# Open a file in write mode and then close it
file = open('example.txt', 'w')
file.close()

# Open a file in append mode and then close it
file = open('example.txt', 'a')
file.close()

# Open a file in binary mode and then close it
file = open('example.bin', 'rb')
file.close()

# Open a file in exclusive creation mode and then close it
file = open('new_file.txt', 'x')
file.close()

# Open a file in update mode and then close it
file = open('example.txt', 'r+')
file.close()
```

## Opening Files in Python

In Python, the `open()` function is used to open a file. It takes the file name and the mode of operation as arguments. The mode specifies how the file should be opened, whether for reading, writing, appending, or creating a new file. Here are the different modes:

- `'r'`: Opens the file for reading.
- `'w'`: Opens the file for writing. Creates a new file if it doesn't exist or overwrites an existing file.
- `'a'`: Opens the file for appending data to it. Creates a new file if it doesn't exist.
- `'x'`: Opens the file for exclusive creation. Creates a new file and fails if the file already exists.

Using `with open()` ensures that the file is closed automatically after the suite finishes executing, making the code cleaner and safer.

### Examples

```python
# Open a file in read mode
with open('example.txt', 'r') as file:
    # Perform operations with the file
    data = file.read()
```

## Writing to Files in Python

The `write()` method is used for writing data into the file. We need to open the file in write mode for writing data into it, and we need to pass `'w'` as the second argument of the `open()` method. When writing to the file, two things can happen:

1. If the file does not exist, then a new file will be created and data will be written into it.
2. If the file already exists, then the whole data of the file will be deleted, and new content will be inserted into it.

A file is opened using the `open()` function, and write mode `'w'` is used to write data to a file. Then, to write a string to a file, `'write'` mode is used. Note that the file's contents will be overwritten by `'w'` mode, while the `'a'` mode will append the data to the end of the file.

```python
# Example of writing to a file in Python

# Open file in write mode ('w')
file_path = 'example.txt'
with open(file_path, 'w') as file:
    # Writing data into the file
    file.write("This is some sample data that we are writing to the file.\n")
    file.write("We can write multiple lines as well.\n")
    file.write("Each write() call adds data to the file.\n")

# Reading the file to verify its content
with open(file_path, 'r') as file:
    content = file.read()
    print("Content of the file:")
    print(content)
```

## Reading Files in Python

The `read()` method is used in Python for reading the file data. To read the file, we need to open it in read mode.

Once a file is opened, you can read its contents using various methods. The most common ones are:

- `read()`: reads entire file as a string.
- `readline()`: reads a single line from the file.
- `readlines()`: reads all lines from the file and returns them as a list.

```python
# Example of reading files in Python

# Reading entire file using read()
file_path = 'example.txt'
with open(file_path, 'r') as file:
    content = file.read()
    print("Content of the file (read()):")
    print(content)

# Reading single line using readline()
with open(file_path, 'r') as file:
    line = file.readline()
    print("\nFirst line of the file (readline()):")
    print(line)

# Reading all lines using readlines()
with open(file_path, 'r') as file:
    lines = file.readlines()
    print("\nAll lines of the file (readlines()):")
    for line in lines:
        print(line.strip())  # strip() is used to remove the newline character at the end of each line
```

## Closing Files in Python

The `close()` method is used in Python for file closing. It is good practice to close the file after performing all operations on it, as it will release all the resources that are bound with the file.

```python

# opening a file
f = open("example.txt", "r")

# reading the data of the file
file_data = f.read()
print(file_data)

# Closing the file
f.close()
```

## Exception Handling in Files

If an exception occurs while working with files, then the program may exit automatically without closing the file. To ensure proper handling of files, it is recommended to use a `try...finally` block. This ensures that the file is closed even if an exception occurs during file operations, thus preventing resource leaks.

```python

try:
    f = open("example.txt", "r")
    file_data = f.read()
    print(file_data)

finally:
    # closing file
    f.close()
```

## Creating and Writing to Files

The `write()` method is used for writing content inside the file. If the file does not exist, it will create a new file and insert content inside it. If the file exists, it will erase all its data and then insert new content inside it.

```python
with open('example2.txt', 'w') as f:
    # write data to the file
    f.write('Hey!!! Welcome')
    
```

## Append Mode in Python File Handling

If the file exists, then append mode inserts the data at the end of the file, without erasing the existing data of the file. It will create a new file if the file does not exist.

```Python
# code to demonstrate the example of append mode

# opening file in append mode
f = open('example.txt', 'a')
f.write("Insert data to demonstrate append mode example")
f.close()
```

## Working with various File Formats

1 . Working with CSV (Comma-Separated Values) Files:

CSV files are basically used to store tabular data. The `csv` module of Python is used for reading CSV files. It allows you to handle various aspects of CSV files, such as reading rows, writing rows, specifying delimiters, handling headers, etc.

```python
import csv

# Writing to a CSV file
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age', 'City'])
    writer.writerow(['John', 30, 'New York'])
    writer.writerow(['Alice', 25, 'Los Angeles'])

# Reading from a CSV file
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

2 . Working with JSON Files:

JSON (JavaScript Object Notation) is a popular format for storing structured data. Python provides the `json` module for working with JSON files. It allows you to load JSON data from a file, convert it to Python objects, and vice versa.

```python
import json

# Writing to a JSON file
data = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}
with open('data.json', 'w') as file:
    json.dump(data, file)

# Reading from a JSON file
with open('data.json', 'r') as file:
    data = json.load(file)
    print(data)
```

3 . Working with Binary Files:

Binary files store data in a binary format, such as images, videos, or executable files. Python allows you to read from and write to binary files using the `'rb'` (read binary) and `'wb'` (write binary) modes.

```python
# Writing to a binary file
with open('binary_data.bin', 'wb') as file:
    file.write(b'Hello, world!')

# Reading from a binary file
with open('binary_data.bin', 'rb') as file:
    data = file.read()
    print(data)
```

4 . File and Directory Manipulation:

The `os` module provides functions for various file and directory operations. You can create, rename, delete files, check if a file exists, get file information, list directory contents, etc.

```python
import os

# Creating a directory
os.mkdir('my_directory')

# Checking if a file exists
if os.path.exists('my_directory'):
    # Creating a file inside the directory
    with open('my_directory/my_file.txt', 'w') as file:
        file.write('Hello, world!')

    # Renaming the file
    os.rename('my_directory/my_file.txt', 'my_directory/renamed_file.txt')

    # Listing directory contents
    print(os.listdir('my_directory'))

    # Deleting the file and directory
    os.remove('my_directory/renamed_file.txt')
    os.rmdir('my_directory')
```

For more methods and in-depth understanding of Python file handling, you can refer to [Scaler Python File Handling Tutorial](https://www.scaler.com/topics/python-file-handling/).
