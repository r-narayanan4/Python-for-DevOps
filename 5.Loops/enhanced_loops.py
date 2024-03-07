# Expanding loops with while-else and for-else

# Using while-else loop
num = 5
while num > 0:
    print(num)
    num -= 1
else:
    print("Loop ended because num is no longer greater than 0")

# Using for-else loop
for i in range(5):
    print(i)
else:
    print("Loop ended successfully")
