from math import sqrt

a = int(input())
b = int(input())
c = int(input())

if a != 0:
    D = b ** 2 - 4 * a * c
    if D > 0:
        x1 = (-b + sqrt(D)) / (2 * a)
        x2 = (-b - sqrt(D)) / (2 * a)
        if x1 > x2:
            print(f"{x1}|{x2}")
        else:
            print(f"{x2}|{x1}")
    elif D == 0:
        x = -b / (2 * a)
        print(f"{x}")
    else:
        print("no real roots")
else:
    if b != 0:
        x = -c / b
        print(f"x = {x}")
    else:
        if c == 0:
            print("special case")
