# Nesting loops and conditional statements

# Nested loops example
for i in range(3):
    for j in range(2):
        print(f"({i}, {j})")

# Nested loop with conditional statement
for i in range(3):
    for j in range(3):
        if i != j:
            print(f"({i}, {j})")
