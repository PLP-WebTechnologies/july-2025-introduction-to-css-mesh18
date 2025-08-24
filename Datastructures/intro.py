#writing a program to check for the largest number among three numbers

a = 5
b = 10
c = 23
if a > b:
    if a > c:
        print(f"{a} is the largest number")
    else:
        print(f"{c} is the largest number")
else:
    if b > c:
        print(f"{b} is the largest number")
    else:
        print(f"{c} is the largest number")