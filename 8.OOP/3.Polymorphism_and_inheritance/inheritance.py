# Inheritance:

# Inheritance is a mechanism that allows us to create a new class - known as a child class - that is based upon an existing class - the parent class.

# Advantages of inheritance:

# This saves you from duplicating a lot of code.

'''

Inheritance in programming is a mechanism where a new class, known as the child class or subclass, can inherit properties and methods 
from an existing class, referred to as the parent class or superclass.

It allows the child class to access and use the attributes and behaviors defined in the parent class without redefining them. 
This promotes code reusability and helps in organizing code in a hierarchical manner.

With inheritance, the child class can extend or modify the functionality of the parent class by adding new attributes or 
methods or by overriding existing ones.

Inheritance simplifies code maintenance by reducing redundancy and promoting a modular approach to software development. 
Changes made in the parent class are automatically reflected in all the child classes that inherit from it, ensuring consistency 
across the codebase.
'''

'''
Inheritance in programming is like passing traits from parents to children. Just like how children inherit traits like eye color or 
height from their parents, in coding, a child class can inherit properties and behaviors from a parent class. 
This means you can create a new class (child) that automatically gets the features of an existing class (parent), saving you from 
rewriting the same code. It helps in organizing and reusing code effectively, making it easier to manage and maintain your programs.
'''

class Tomcat(object):  # Superclass or Parent class
    def __init__(self, home, ver):
        # Initializing attributes for Tomcat class
        self.home = home
        self.version = ver
    
    def display(self):
        # Method to display home and version
        print(self.home)
        print(self.version)

class Apache(Tomcat):  # Subclass or Child class
    def __init__(self, home, ver):
        # Initializing attributes for Apache class
        # Calling the __init__ method of the parent class (Tomcat) to initialize its attributes
        super().__init__(home, ver)
        
# Creating objects of Tomcat and Apache classes
tom_ob = Tomcat('/home/tomcat9', '7.6')  # Object of Parent class
apa_ob = Apache("/etc/httpd", '2.4')  # Object of Child class

# Calling the display method for both objects
tom_ob.display()  # Displaying Tomcat object
apa_ob.display()  # Displaying Apache object
