def plus_one(digits: list):
    num = int(''.join(map(str, digits)))
    num += 1
    result = [int(d) for d in str(num)]
    return result


print(plus_one([1, 2, 3, 4]))
