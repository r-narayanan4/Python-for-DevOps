# Program to find the largest among three numbers using nested if-else statements

# Define the three numbers
x = 15
y = 20
z = 10

# Check if x is greater than y
if x > y:
    # If x is greater than y, check if it's also greater than z
    if x > z:
        print("x is the largest")
    else:
        print("z is the largest")
# If x is not greater than y, check if y is greater than z
else:
    # If y is greater than z, y is the largest
    if y > z:
        print("y is the largest")
    # If y is not greater than z, z is the largest
    else:
        print("z is the largest")
