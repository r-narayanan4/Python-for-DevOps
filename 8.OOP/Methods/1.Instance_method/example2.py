# Example 2: Creating a Car class to print the specifications of a particular car using instance methods.

class Car:
    # Initialize the Car object with the make, model, and year
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        # Set the odometer reading to 0
        self.odometer = 0

    # Method to simulate driving the car and add to the odometer reading
    def drive(self, miles):
        self.odometer += miles

    # Method to return the car's info including make, model, year, and odometer reading
    def get_info(self):
        return f"{self.year} {self.make} {self.model} with {self.odometer} miles"

# Create an instance of the Car class with a make of "Toyota", model of "Corolla", and year of 2022
my_car = Car("Toyota", "Corolla", 2022)

# Simulate driving the car for 50 miles
my_car.drive(50)

# Print the car's info
print(my_car.get_info())
