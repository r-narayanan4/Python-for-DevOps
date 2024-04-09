# importing os module
import os

# method for file creation
def file_creation(file_name):
  try: 
    with open(file_name, 'w') as file:
      file.write('Hey!!! Welcome...')
    print("File Creation Successful")
  except IOError:
    print("Error!! File creation failed")

# method for reading data from the file
def file_reading(file_name):
  try: 
    with open(file_name, 'r') as file:
      file_content = file.read()
      print(file_content)
    print("File Reading Successful")
  except IOError:
    print("Error!! File reading failed")


# method for appending data into the file
def data_appending(file_name, data):
  try: 
    with open(file_name, 'a') as file:
      file.write(data)
    print("Appended Data Successfully")
  except IOError:
    print("Error!! Data appending failed")


# method for renaming file
def file_renaming(file_name, new_name):
  try: 
    os.rename(file_name, new_name)
    print("File Renaming Successful")
  except IOError:
    print("Error!! Data renaming failed")


# method for deletion of file
def file_deletion(file_name):
  try: 
    os.remove(file_name)
    print("File Deletion Successful")
  except IOError:
    print("Error!! Data Deletion failed")

 
if __name__ == '__main__':
    file_name = "example1.txt"
    new_name = "example2.txt"
 
    file_creation(file_name)
    file_reading(file_name)
    data_appending(file_name, "Add data to demonstrate appending data")
    file_reading(file_name)
    file_renaming(file_name, new_name)
    file_reading(new_name)
    file_deletion(new_name)
