# Importing ABC (Abstract Base Class) and abstractmethod from the abc module
from abc import ABC, abstractmethod

# Defining an abstract base class named Vehicle, inheriting from ABC
class Vehicle(ABC):  
    # Constructor method for the Vehicle class
    def __init__(self, n):
        # Initializing an instance variable no_of_tyres with the value of n
        self.no_of_tyres = n
    
    # Abstract method named start, marked by using the @abstractmethod decorator
    @abstractmethod  
    def start(self):
        # Placeholder pass statement, indicating that this method must be implemented by subclasses
        pass
    
    # Concrete method named display
    def display(self):
        # Printing a message
        print("Hi I am calling from vehicle class ")
