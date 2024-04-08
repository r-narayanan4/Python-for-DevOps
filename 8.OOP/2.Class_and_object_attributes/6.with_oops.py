#!/bin/python3
import os

class Tomcat(object):
    def get_home_conf_file(self, server_xml):
        """
        Method to set the Tomcat home directory and configuration file path.

        Args:
            server_xml (str): The path to the server.xml file.

        Returns:
            None
        """
        self.t_home = os.path.dirname(os.path.dirname(server_xml))
        self.conf_file = server_xml
        return None

    def display_details(self):
        """
        Method to display Tomcat details.

        Returns:
            None
        """
        print("Tomcat home is: ", self.t_home)
        print("Tomcat conf file is: ", self.conf_file)
        return None

def get_all_tomcats():
    """
    Function to find all server.xml files in the system.

    Returns:
        list: A list containing paths to all server.xml files found.
    """
    list_of_config_files = []
    for r, d, f in os.walk("/"):
        for each_file in f:
            if each_file == 'server.xml':
                list_of_config_files.append(os.path.join(r, each_file))
    return list_of_config_files

def main():
    # Finding list of tomcats
    print("Finding list of tomcats...")
    list_of_tomcats = get_all_tomcats()
    tomcat_objects = []
    for each_file in list_of_tomcats:
        tomcat_object = Tomcat()
        tomcat_object.get_home_conf_file(each_file)
        tomcat_objects.append(tomcat_object)
    for each_ob in tomcat_objects:
        each_ob.display_details()

    return None

if __name__ == '__main__':
    main()
