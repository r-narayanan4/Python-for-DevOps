# Procedural Programming Concepts

# Suppose if you implement any code in terms of functions, then we can say that we are following procedural oriented programing concepts.


import os  # Importing the os module for interacting with the operating system

# Function to extract details for each Tomcat instance
def get_details_for_each_tomcat(server_xml):
    tcf = server_xml  # Storing the path of the server.xml file
    th = os.path.dirname(os.path.dirname(server_xml))  # Extracting the Tomcat home directory
    return tcf, th  # Returning the Tomcat config file path and home directory path

# Function to display Tomcat details
def display_details(tcf, th):
    print(f'The tomcat config file is: {tcf}\nThe tomcat home is: {th}')  # Printing Tomcat config file and home directory

# Main function
def main():
    # Getting details for Tomcat 7 and Tomcat 9 instances
    tomcat7_details = get_details_for_each_tomcat("/home/Automation/tomcat7/conf/server.xml")
    tomcat9_details = get_details_for_each_tomcat("/home/Automation/tomcat9/conf/server.xml")

    # Displaying details for Tomcat 7 and Tomcat 9 instances
    display_details(*tomcat7_details)
    display_details(*tomcat9_details)

# Checking if the script is run directly
if __name__ == "__main__":
    main()  # Calling the main function if the script is run directly
