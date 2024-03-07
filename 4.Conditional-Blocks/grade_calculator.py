# Program to calculate grades based on marks using if-elif-else

# Input
marks = float(input("Enter your marks: "))

# Calculating grade based on marks
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: F (Fail)")
