def number_pow(number, pow):
    if pow == 0:
        return 1
    return number * number_pow(number, pow - 1)


num, power = map(int, input().split())

print(number_pow(num, power))


