# Prompt the user for their conversion choice
choice = input("Enter 'C' to convert from Celsius to Fahrenheit or 'F' to convert from Fahrenheit to Celsius: ")

# Check the user's choice and perform the conversion accordingly
if choice == 'C':  # If the user chooses to convert from Celsius to Fahrenheit
    celsius = float(input("Enter the temperature in Celsius: "))  # Prompt the user for the temperature in Celsius
    fahrenheit = (celsius * 9/5) + 32  # Perform the conversion
    print("Temperature in Fahrenheit:", fahrenheit)  # Display the result
elif choice == 'F':  # If the user chooses to convert from Fahrenheit to Celsius
    fahrenheit = float(input("Enter the temperature in Fahrenheit: "))  # Prompt the user for the temperature in Fahrenheit
    celsius = (fahrenheit - 32) * 5/9  # Perform the conversion
    print("Temperature in Celsius:", celsius)  # Display the result
else:  # If the user's choice is invalid
    print("Invalid choice")  # Display an error message
