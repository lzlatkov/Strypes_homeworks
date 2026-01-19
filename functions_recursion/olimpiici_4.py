def is_palindrome(txt):
    if len(txt) <= 1:
        return True
    if txt[0] != txt[-1]:
        return False
    return is_palindrome(txt[1:-1])


user_input = input()

print(is_palindrome(user_input))
