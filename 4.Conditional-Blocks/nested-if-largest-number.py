# Program to find the largest among four numbers using nested if-else statements

a = 10
b = 15
c = 20
d = 5

if a > b:
    if a > c:
        if a > d:
            print("a is the largest")
        else:
            print("d is the largest")
    else:
        if c > d:
            print("c is the largest")
        else:
            print("d is the largest")
else:
    if b > c:
        if b > d:
            print("b is the largest")
        else:
            print("d is the largest")
    else:
        if c > d:
            print("c is the largest")
        else:
            print("d is the largest")
