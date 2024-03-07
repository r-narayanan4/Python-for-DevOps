# Simple Number Triangle Pattern
rows = 5
print("Simple Number Triangle Pattern:")
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Inverted Pyramid Pattern
rows = 5
print("\nInverted Pyramid Pattern:")
for i in range(rows, 0, -1):
    for j in range(0, rows - i):
        print(end=" ")
    for j in range(0, i):
        print("*", end=" ")
    print()

# Half Pyramid Pattern
rows = 5
print("\nHalf Pyramid Pattern:")
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print()

# Inverted Pyramid Pattern
rows = 5
print("\nInverted Pyramid Pattern:")
for i in range(rows, 0, -1):
    for j in range(0, rows - i):
        print(end=" ")
    for j in range(0, i):
        print("*", end=" ")
    print()

# Reverse Pyramid Pattern
rows = 5
print("\nReverse Pyramid Pattern:")
for i in range(rows, 0, -1):
    for j in range(0, rows - i):
        print(end=" ")
    for j in range(0, i):
        print("*", end=" ")
    print()

# Half Inverted Pyramid Pattern
rows = 5
print("\nHalf Inverted Pyramid Pattern:")
for i in range(rows, 0, -1):
    for j in range(0, i):
        print("*", end=' ')
    print()

# Pyramid of Natural Numbers Less Than 10
rows = 5
num = 1
print("\nPyramid of Natural Numbers Less Than 10:")
for i in range(0, rows):
    for j in range(0, i + 1):
        print(num, end=" ")
        num += 1
    print()

# Mirrored Pyramid Pattern
rows = 5
print("\nMirrored Pyramid Pattern:")
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print()
for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print()

# Inverted Pyramid of the Same Digit
rows = 5
num = 5
print("\nInverted Pyramid of the Same Digit:")
for i in range(rows, 0, -1):
    for j in range(0, i):
        print(num, end=' ')
    print()
