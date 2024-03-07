# Controlling loop execution with break and continue

# Using break statement to exit loop early
print("Using break statement:")
for i in range(10):
    if i == 5:
        break
    print(i)

# Using continue statement to skip iteration
print("\nUsing continue statement:")
for i in range(5):
    if i == 2:
        continue
    print(i)
