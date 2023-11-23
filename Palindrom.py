def check_palindrome(num):
    return str(num) == str(num)[::-1]


print(check_palindrome(121))
