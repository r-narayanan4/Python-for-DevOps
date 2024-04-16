# Importing necessary modules
import os
import string
import platform

# Asking user to input the file name to search
req_file = input("Enter your file name to search: ")

# Checking the operating system
if platform.system() == "Windows":
    # Generating a list of all available drive names in Windows
    pd_names = string.ascii_uppercase
    vd_names = []
    for each_drive in pd_names:
        if os.path.exists(each_drive + ":\\"):
            vd_names.append(each_drive + ":\\")
    print(vd_names)

    # Searching for the file in each drive
    for each_drive in vd_names:
        for r, d, f in os.walk(each_drive):
            for each_f in f:
                if each_f == req_file:
                    print(os.path.join(r, each_f))
else:
    # Searching for the file starting from the root directory ("/") in Unix-like systems
    for r, d, f in os.walk("/"):
        for each_file in f:
            if each_file == req_file:
                print(os.path.join(r, each_file))
