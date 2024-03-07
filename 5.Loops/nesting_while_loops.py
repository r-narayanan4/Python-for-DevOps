# Outer loop using 'while' loop to iterate from 1 to 5
i = 1
while i <= 5:
    # Inner loop using 'while' loop to iterate from 1 to i
    j = 1
    while j <= i:
        print(j, end=" ")
        # Increment inner loop counter
        j += 1
    # Move to the next line after printing inner loop values
    print()
    # Increment outer loop counter
    i += 1
