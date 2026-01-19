user_input = input().strip().lower()
histogram = {}

# for ch in user_input:
#     histogram[ch] = histogram.get(ch, 0) + 1
#
# print(sorted(histogram.items()))
for ch in user_input:
    if ch in histogram:
        histogram[ch] += 1
    else:
        histogram[ch] = 1

result = sorted(histogram.items())

print(result)
