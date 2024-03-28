# Assign value
x = 10
print("x after assigning value using '=':", x)  # Output: x after assigning value using '=': 10

# Add and assign
x += 5
print("x after adding and assigning using '+=':", x)  # Output: x after adding and assigning using '+=': 15

# Subtract and assign
x -= 3
print("x after subtracting and assigning using '-=':", x)  # Output: x after subtracting and assigning using '-=': 12

# Multiply and assign
x *= 2
print("x after multiplying and assigning using '*=':", x)  # Output: x after multiplying and assigning using '*=': 24

# Divide and assign
x /= 4
print("x after dividing and assigning using '/=':", x)  # Output: x after dividing and assigning using '/=': 6.0

# Modulus and assign
x %= 3
print("x after modulus and assigning using '%=':", x)  # Output: x after modulus and assigning using '%=': 0.0

# Exponentiation and assign
x **= 2
print("x after exponentiation and assigning using '**=':", x)  # Output: x after exponentiation and assigning using '**=': 0.0

# Floor division and assign
x //= 2
print("x after floor division and assigning using '//=':", x)  # Output: x after floor division and assigning using '//=': 0.0



print("\nNew program for assignment operator")

# Get user input for initial value of x
x = int(input("Enter the initial value of x: "))
print("Initial value of x:", x)

# Get user input for value to add and assign
add_value = int(input("Enter the value to add and assign to x: "))
x += add_value
print("x after adding and assigning:", x)

# Get user input for value to subtract and assign
subtract_value = int(input("Enter the value to subtract and assign from x: "))
x -= subtract_value
print("x after subtracting and assigning:", x)

# Get user input for value to multiply and assign
multiply_value = int(input("Enter the value to multiply and assign to x: "))
x *= multiply_value
print("x after multiplying and assigning:", x)

# Get user input for value to divide and assign
divide_value = int(input("Enter the value to divide and assign from x: "))
x /= divide_value
print("x after dividing and assigning:", x)

# Get user input for value to perform modulus and assign
modulus_value = int(input("Enter the value for modulus and assign to x: "))
x %= modulus_value
print("x after modulus and assigning:", x)

# Get user input for value to perform exponentiation and assign
exponent_value = int(input("Enter the value for exponentiation and assign to x: "))
x **= exponent_value
print("x after exponentiation and assigning:", x)

# Get user input for value to perform floor division and assign
floor_division_value = int(input("Enter the value for floor division and assign to x: "))
x //= floor_division_value
print("x after floor division and assigning:", x)


