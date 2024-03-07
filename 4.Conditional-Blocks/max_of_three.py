# Program to find the maximum of three numbers using if-elif

# Input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Finding the maximum among the three numbers
if num1 >= num2 and num1 >= num3:
    print("Max:", num1)
elif num2 >= num1 and num2 >= num3:
    print("Max:", num2)
else:
    print("Max:", num3)
