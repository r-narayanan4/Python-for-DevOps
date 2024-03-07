# Program to classify a given character as uppercase, lowercase, or special symbol using nested if-else statements

char = '&'

if char.isalpha():
    if char.islower():
        print(char, "is a lowercase letter.")
    else:
        print(char, "is an uppercase letter.")
else:
    print(char, "is a special symbol.")
