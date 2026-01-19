def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        memo[n] = n
    else:
        memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]


start_index, end_index = map(int, input().split())

fibonacci_list = [fibonacci(i) for i in range(start_index - 1, end_index)]

print(*fibonacci_list)
