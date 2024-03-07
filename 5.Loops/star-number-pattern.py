# Simple Asterisk Triangle Pattern
rows = 5
print("Simple Asterisk Triangle Pattern:")
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

# Inverted Asterisk Pyramid Pattern
rows = 5
print("\nInverted Asterisk Pyramid Pattern:")
for i in range(rows, 0, -1):
    for j in range(0, rows - i):
        print(end=" ")
    for j in range(0, i):
        print("*", end=" ")
    print()

# Half Asterisk Pyramid Pattern
rows = 5
print("\nHalf Asterisk Pyramid Pattern:")
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print()

# Inverted Asterisk Pyramid Pattern
rows = 5
print("\nInverted Asterisk Pyramid Pattern:")
for i in range(rows, 0, -1):
    for j in range(0, rows - i):
        print(end=" ")
    for j in range(0, i):
        print("*", end=" ")
    print()

# Reverse Asterisk Pyramid Pattern
rows = 5
print("\nReverse Asterisk Pyramid Pattern:")
for i in range(rows, 0, -1):
    for j in range(0, rows - i):
        print(end=" ")
    for j in range(0, i):
        print("*", end=" ")
    print()

# Half Inverted Asterisk Pyramid Pattern
rows = 5
print("\nHalf Inverted Asterisk Pyramid Pattern:")
for i in range(rows, 0, -1):
    for j in range(0, i):
        print("*", end=' ')
    print()

# Pyramid of Asterisks Less Than 10
rows = 5
print("\nPyramid of Asterisks Less Than 10:")
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=" ")
    print()

# Mirrored Asterisk Pyramid Pattern
rows = 5
print("\nMirrored Asterisk Pyramid Pattern:")
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print()
for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print()

# Inverted Asterisk Pyramid of the Same Digit
rows = 5
num = 5
print("\nInverted Asterisk Pyramid of the Same Digit:")
for i in range(rows, 0, -1):
    for j in range(0, i):
        print("*", end=' ')
    print()
