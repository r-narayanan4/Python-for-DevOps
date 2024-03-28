# Method 1: Using range() function
print("Loop using range():")
for i in range(5):
    print(i, end=" ")
print()

# Method 2: Iterating over a list directly
print("Loop using list:")
my_list = [1, 2, 3, 4, 5]
for item in my_list:
    print(item, end=" ")
print()

# Method 3: Using list comprehension
print("Loop using list comprehension:")
squared_numbers = [x * x for x in range(1, 6)]
for num in squared_numbers:
    print(num, end=" ")
print()

# Method 4: Iterating over a string
print("Loop over string:")
my_string = "hello"
for char in my_string:
    print(char, end=" ")
print()

# Method 5: Nested loops
print("Nested loops:")
for i in range(3):
    for j in range(2):
        print(i, j)
