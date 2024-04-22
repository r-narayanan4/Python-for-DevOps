# Importing necessary modules
import os
import sys
import datetime

# Getting user input for the path
req_path = input("Enter your path: ")

# Specifying the age in days
age = 3

# Checking if the provided path exists
if not os.path.exists(req_path):
    print("Please provide a valid path.")
    sys.exit(1)

# Checking if the provided path is a file
if os.path.isfile(req_path):
    print("Please provide a directory path.")
    sys.exit(2)

# Getting the current date
today = datetime.datetime.now()

# Iterating through each file in the directory
for each_file in os.listdir(req_path):
    # Constructing the full file path
    each_file_path = os.path.join(req_path, each_file)
    
    # Checking if the item is a file
    if os.path.isfile(each_file_path):
        # Getting the creation date of the file
        file_cre_date = datetime.datetime.fromtimestamp(os.path.getctime(each_file_path))
        
        # Calculating the difference in days between today and the creation date of the file
        dif_days = (today - file_cre_date).days
        
        # Checking if the file is older than the specified age
        if dif_days > age:
            print(each_file_path, dif_days)
