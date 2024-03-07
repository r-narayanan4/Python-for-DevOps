# Using the pass instruction

# The pass instruction is a null operation; nothing happens when it executes.
# It can be used as a placeholder when a statement is syntactically required but you don’t want any code to execute.

# Example:
for i in range(5):
    if i == 3:
        pass  # Placeholder, does nothing
    else:
        print(i)
