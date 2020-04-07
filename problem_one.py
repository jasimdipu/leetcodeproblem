def singleNumber(list):
    x = 0
    for a in lst:
        x ^= a

    return x


lst = [2, 2, 1, 1, 10, 10, 15]

print(singleNumber(lst))
