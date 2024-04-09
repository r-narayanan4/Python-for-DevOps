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
    