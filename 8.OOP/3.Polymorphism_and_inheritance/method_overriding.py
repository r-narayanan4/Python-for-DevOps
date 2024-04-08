# same example as polymorphism.py

# Polymorphism:
# Polymorphism allows us to define the same methods name  in different classes.
# This process is also known as method overriding (simply we are overwriting the same method in different classes).
# Method overriding is a way to achieve runtime polymorphism.
# Polymorphism can be achieved through method overriding, where the actual method call is determined at runtime based on the object type.
# Defining the same method name in different classes is nothing but polymorphism.


class Tomcat(object):
    # Constructor for Tomcat class
    def __init__(self, home, ver):
        # Initialize instance variables home and version
        self.home = home  # home directory of Tomcat
        self.version = ver  # version of Tomcat
        return None  # This return statement is unnecessary
    
    # Method to display information about Tomcat
    def display(self):
        print("This is from tocmat class")  # Display message indicating class name
        print(self.home)  # Display home directory
        print(self.version)  # Display version
        return None  # This return statement is unnecessary

class Apache(object):
    # Constructor for Apache class
    def __init__(self, home, ver):
        # Initialize instance variables home and version
        self.home = home  # home directory of Apache
        self.version = ver  # version of Apache
        return None  # This return statement is unnecessary
    
    # Method to display information about Apache
    def display(self):
        print("This is from apache class")  # Display message indicating class name
        print(self.home)  # Display home directory
        print(self.version)  # Display version
        return None  # This return statement is unnecessary

# Creating instances of Tomcat and Apache classes
tom_ob = Tomcat('/home/tomcat9', '7.6')  # Creating Tomcat object with home directory '/home/tomcat9' and version '7.6'
apa_ob = Apache("/etc/httpd", '2.4')  # Creating Apache object with home directory '/etc/httpd' and version '2.4'

# Calling display method for each object to print information
tom_ob.display()  # Printing information about Tomcat object
apa_ob.display()  # Printing information about Apache object
