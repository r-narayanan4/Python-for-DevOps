# Importing the Vehicle class from the abstract_class module
from abstract_class import Vehicle

# Definition of the Bike class, inheriting from the Vehicle class
class Bike(Vehicle):
    # Constructor method for the Bike class
    def __init__(self, n, color):
        # Calling the constructor of the parent class (Vehicle) using super() and passing the number of tyres (n)
        super().__init__(n)
        # Initializing the color attribute of the Bike class
        self.color = color

    # Implementation of the start method for the Bike class
    def start(self):
        # Printing a message indicating how the bike starts
        print("Start with Kick")

    # Overriding the display method inherited from the Vehicle class
    def display(self):
        # Printing a message displaying the color of the bike
        print(f"My color is {self.color}")

# Definition of the Scooty class, inheriting from the Vehicle class
class Scooty(Vehicle):
    # Implementation of the start method for the Scooty class
    def start(self):
        # Printing a message indicating how the scooty starts
        print("Self start")

# Definition of the Car class, inheriting from the Vehicle class
class Car(Vehicle):
    # Constructor method for the Car class
    def __init__(self, n, no_of_gears):
        # Calling the constructor of the parent class (Vehicle) using super() and passing the number of tyres (n)
        super().__init__(n)
        # Initializing the no_of_gears attribute of the Car class
        self.no_of_gears = no_of_gears

    # Implementation of the start method for the Car class
    def start(self):
        # Printing a message indicating how the car starts
        print("Start with key")
