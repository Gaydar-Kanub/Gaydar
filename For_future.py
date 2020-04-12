# разложение числа на множители (удобно при приведении к общему знаминателю)
def divide(num):
    n = 2
    res = []
    while num > 1:
        if num % n == 0:
            res.append(n)
            num = num // n
            continue
        else:
            n += 1
    return res

print(divide(10080))