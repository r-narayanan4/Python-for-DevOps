"""
os.system() from the os module:

The os.system() function is used to execute operating system commands from within a Python script.

Concept Explanation:

- os.system() is a function provided by the os module in Python.
- It allows you to run shell commands directly from your Python script.
- This function is useful when you need to execute operating system commands that are not directly available as Python functions or methods.
- It takes a string argument, which is the command to be executed in the shell.
- The command is passed to the default system shell (e.g., Bash on Unix-like systems or Command Prompt on Windows), and the output is displayed in the terminal.
- The return value of os.system() is the exit status of the command executed. It returns 0 if the command was successful, and a non-zero value otherwise.
- It's important to be cautious when using os.system(), especially with user input, to avoid security vulnerabilities such as command injection.
- Example Usage: os.system("ls") executes the "ls" command (list files and directories) on Unix-like systems, and the output is displayed in the terminal.

In summary, os.system() provides a way to interact with the operating system from within a Python script, allowing you to execute shell commands seamlessly.
"""
import os

# Program 1: Error Handling for os.system()

# Command to be executed
command = "date"

# Execute the command using os.system()
exit_code = os.system(command)

# Check the exit code to determine if the command executed successfully
if exit_code == 0:
    print(f"Command '{command}' executed successfully.")
else:
    print(f"Error executing command '{command}'. Exit code: {exit_code}")

# Program 2: Error Handling for File Existence Checking

# Path to check for existence
path = "/path/to/file"

# Check if the file exists
if os.path.exists(path):
    print(f"The file '{path}' exists.")
else:
    print(f"The file '{path}' does not exist.")
