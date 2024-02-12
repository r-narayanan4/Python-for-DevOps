# Using is operator : Returns true if both variables are the same object
# Define two variables with the same value

x = 5
y = 5

# Check if x and y are the same object
if x is y:
    print("x and y are the same object")
else:
    print("x and y are not the same object")


# Define two lists
list1 = [1, 2, 3]
list2 = [1, 2, 3]

# Check if list1 and list2 are the same object
if list1 is list2:
    print("list1 and list2 are the same object")
else:
    print("list1 and list2 are not the same object")

"""
In Python, when you create a list (or any other mutable object), it is stored in memory, and the variable you assign it to holds a reference to that memory location. When you define list1 = [1, 2, 3] and list2 = [1, 2, 3], Python creates two separate list objects with the same values [1, 2, 3]. Despite having identical values, they occupy different memory locations.

When you use the is operator to compare list1 and list2, it checks if they refer to the same memory location. Since list1 and list2 were created independently, they are stored in different memory locations. Thus, list1 is list2 evaluates to False, indicating that list1 and list2 are not the same object.

"""

# Using is not operator : Returns true if both variables are not the same object

# Define two strings
string1 = "hello"
string2 = "world"

# Check if string1 and string2 are not the same object
if string1 is not string2:
    print("string1 and string2 are not the same object")
else:
    print("string1 and string2 are the same object")

value1 = "rln"
value2 = "rln"

if value1 is not value2:
    print("value1 and value2 are not the same object")
else:
    print("value1 and value2 are same")

