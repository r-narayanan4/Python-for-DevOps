# Program to check if a year is a leap year using if-elif-else

# Input
year = int(input("Enter a year: "))

# Checking if the year is a leap year or not
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")
