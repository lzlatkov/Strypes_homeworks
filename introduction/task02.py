a = int(input())
b = int(input())

while b != 0:
    last_b = b
    b = a % b
    a = last_b
print(f"Най-големият общ делител е: {a}")
