# Logical AND (and) : This operator returns True if both the operands are true, otherwise, it returns False

# Example 1
x = 5
y = 10
z = 15

if x > 0 and y > 0:
    print("Both x and y are positive.")

# Example 2
if x < 0 and z > 0:
    print("This won't be printed since x is not negative.")


# Logical OR (or) : This operator returns True if either of the operands is true, otherwise, it returns False.

# Example 1
temperature = 25

if temperature > 30 or temperature < 0:
    print("Extreme weather condition!")

# Example 2
name = "Alice"

if name == "Alice" or name == "Bob":
    print("Hello, welcome!")


# Logical NOT (not): This operator returns True if the operand is false and vice versa.
    

# Example 1
is_raining = False

if not is_raining:
    print("It's not raining. Enjoy the weather!")

# Example 2
age = 18

if not age >= 21:
    print("You are not eligible to drink alcohol.")

# Example: Checking if a number is not equal to zero
number = 5

if not number == 0:
    print("The number is not zero.")
else:
    print("The number is zero.")
