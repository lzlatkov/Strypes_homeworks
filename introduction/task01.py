
a = int(input())
b = int(input())
c = int(input())

if a + b > c and a + c > b and b + c > a:
    print(f"Съществува триъгълник със страни {a}, {b}, {c}")
else:
    print(f"Не съществува триъгълник със страни {a}, {b}, {c}")
