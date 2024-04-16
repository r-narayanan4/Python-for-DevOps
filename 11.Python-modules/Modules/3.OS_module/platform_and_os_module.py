# Pratice withplatform and os module 

# write a single python script to clear terminal of any operating system or write a platform independent script to clear terminal

import os
import platform

# Check the operating system using platform module
if platform.system() == "Windows":
    # Clear the terminal in Windows using "cls" command
    os.system("cls")
else:
    # Clear the terminal in Unix-like systems using "clear" command
    os.system("clear")
