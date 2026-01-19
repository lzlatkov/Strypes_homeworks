data = input().split()
unique = []

for x in data:
    if x not in unique:
        unique.append(x)

print(' '.join(unique))
