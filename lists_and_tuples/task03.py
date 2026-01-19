data = input().split()

has_duplicates = False

for i in range(len(data)):
    for j in range(i + 1, len(data)):
        if data[i] == data[j]:
            has_duplicates = True
            break
    if has_duplicates:
        break

print(has_duplicates)


