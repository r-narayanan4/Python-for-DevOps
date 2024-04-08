from abstract_demo import *

# Additional print statement for readability
print("Creating a Bike:")
# Creating an instance of Bike with 2 tyres and color black
bike = Bike(2, "black")
# Printing the number of tyres for the bike instance
print("Number of Tyres for Bike:", bike.no_of_tyres)
# Additional print statement for readability
print("Starting the Bike:")
# Calling the start method of the bike instance
bike.start()
# Additional print statement for readability
print("Displaying Bike information:")
# Calling the display method of the bike instance
bike.display()
# Additional print statement for readability
print("\n")

# Additional print statement for readability
print("Creating a Scooty:")
# Creating an instance of Scooty with 2 tyres
scooty = Scooty(2)
# Additional print statement for readability
print("Starting the Scooty:")
# Calling the start method of the scooty instance
scooty.start()
# Additional print statement for readability
print("Displaying Scooty information:")
# Since the display method is not defined in the Scooty class, it will call the display method inherited from the Vehicle class
scooty.display()
# Additional print statement for readability
print("\n")

# Additional print statement for readability
print("Creating a Car:")
# Creating an instance of Car with 4 tyres and 6 gears
car = Car(4, 6)
# Additional print statement for readability
print("Starting the Car:")
# Calling the start method of the car instance
car.start()
# Printing the number of gears for the car
print("Number of Gears:", car.no_of_gears)
