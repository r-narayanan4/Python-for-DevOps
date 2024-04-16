"""
getpass module

The getpass module provides a secure way to handle password prompts when programs interact with users via the terminal. It consists of two important functions: getpass() and getuser().

- getpass():
    This function prompts the user for a password without echoing characters on the terminal. It's commonly used when a program needs to securely collect passwords from users.
    
- getuser():
    The getuser() function returns the login name of the user. It checks the environment variables LOGNAME, USER, LNAME, and USERNAME in order and returns the value of the first non-empty string. This function can be used to retrieve the username of the currently logged-in user.

"""

import getpass

def main():
    # Prompt the user to enter a password without echoing characters
    # db_pass=getpass.getpass() # default prompt it will ask password
    db_pass = getpass.getpass(prompt="Enter your db_password:")
    print(f"The Entered password is: {db_pass}")

    # Get the login name of the user
    user_name = getpass.getuser()
    print(f"Logged-in User: {user_name}")

if __name__ == "__main__":
    main()
