from math import sqrt

a = int(input())
b = int(input())
c = int(input())

if a != 0:

    D = b ** 2 - 4 * a * c
    if D > 0:
        x1 = (-b + sqrt(D)) / (2 * a)
        x2 = (-b - sqrt(D)) / (2 * a)
        print(f"Реални корени: x1 = {x1}, x2 = {x2}")
    elif D == 0:
        x = -b / (2 * a)
        print(f"Двойни корени: x = {x}")
    else:
        print("Няма реални корени")
else:

    if b != 0:
        x = -c / b
        print(f"x = {x}")
    else:
        if c == 0:
            print("Особен случай")


