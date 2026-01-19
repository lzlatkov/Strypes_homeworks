alphabet = "abcdefghijklmnopqrstuvwxyz"


text, key = input().lower().split()

result = ""
key_index = 0

for char in text:
    if char in alphabet:
        t_index = alphabet.index(char)
        k_index = alphabet.index(key[key_index % len(key)])
        result += alphabet[(t_index + k_index) % 26]
        key_index += 1

print(result)
