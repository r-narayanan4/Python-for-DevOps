import os

# Define a class named Tomcat
class Tomcat:
    # Method to get details for each Tomcat instance
    def get_details_for_each_tomcat(self, server_xml):
        self.tcf = server_xml  # Store the path of the server.xml file in the object attribute tcf
        self.th = os.path.dirname(os.path.dirname(server_xml))  # Extract the Tomcat home directory
        return None  # No meaningful return value

    # Method to display Tomcat details
    def display_details(self):
        print(f'The tomcat config file is: {self.tcf}\nThe tomcat home is: {self.th}')
        return None  # No meaningful return value

# Main function
def main():
    # Create two instances (objects) of the Tomcat class
    tomcat7 = Tomcat()
    tomcat9 = Tomcat()

    # Call the get_details_for_each_tomcat method for each Tomcat instance to set their attributes
    tomcat7.get_details_for_each_tomcat("/home/Automation/tomcat7/conf/server.xml")
    #get_details_for_each_tomcat('tomcat7',"/home/Automation/tomcat7/conf/server.xml") it will  convert like this 
    tomcat9.get_details_for_each_tomcat("/home/Automation/tomcat9/conf/server.xml")
    #get_details_for_each_tomcat('tomcat9',"/home/Automation/tomcat9/conf/server.xml") 
    

    #print(tomcat9.tcf)
	#print(tomcat7.th)
	#print(tomcat9.th)
	#print(tomcat7.tcf)

    # Call the display_details method for each Tomcat instance to display their details
    tomcat7.display_details()
    #display_details('tomcat7')
    tomcat9.display_details()

    #display_details('tomcat9')

    return None  # No meaningful return value

# Check if the script is run directly
if __name__ == "__main__":
    main()  # Call the main function if the script is run directly
