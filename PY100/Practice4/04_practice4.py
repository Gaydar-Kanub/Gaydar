def num_sys_10_2_001(dec=None):
    if dec is None:
        print('Введите число для перевода его из десятеричной сист.счисления в двоичную сист.счисления')
        dec = int(input())
    binary = ''
    if dec == 0:
        return '0'
    while dec > 0:
        binary += str(dec % 2)
        dec = dec // 2
    return binary[::-1]


# print(num_sys_10_2_001())


def num_sys_2_10_002(binary=None):
    if binary is None:
        print('Введите число для перевода его из двоичной сист.счисления в десятеричную сист.счисления')
        binary = input()
    dec = 0
    for i in range(len(binary)):
        dec += int(binary[-i-1]) * 2 ** i
    return dec


# print(num_sys_2_10_002())


def num_sys_16_10_003(hexa=None):
    if hexa is None:
        print('Введите число для перевода его из шестнадцатиричной сист.счисления в десятеричную сист.счисления')
        hexa = input()
    dec = 0
    liter = ('a', 'b', 'c', 'd', 'e', 'f')
    for i in range(len(hexa)):
        num = hexa[-i-1]
        if num in liter:
            num = 10 + liter.index(num)
        dec += int(num) * 16 ** i
    return dec


# print(num_sys_16_10_003())


def num_sys_10_16_004(dec=None):
    if dec is None:
        print('Введите число для перевода его из десятеричной сист.счисления в шестнадцатиричную сист.счисления')
        dec = int(input())
    hexa = ''
    liter = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f')
    if dec == 0:
        return '0'
    while dec > 0:
        hexa += liter[dec % 16]
        dec = dec // 16
    return hexa[::-1]


# print(num_sys_10_16_004())


def num_sys_16_2_005():
    print('Введите число для перевода его из шестнадцатиричной сист.счисления в двоичную сист.счисления')
    hexa = input()
    dec = num_sys_16_10_003(hexa)
    binary = num_sys_10_2_001(dec)
    return binary


# print(num_sys_16_2_005())


def num_sys_2_16_006():
    print('Введите число для перевода его из двоичной сист.счисления в шестнадцатиричную сист.счисления')
    binary = input()
    dec = num_sys_2_10_002(binary)
    hexa = num_sys_10_16_004(dec)
    return hexa


# print(num_sys_2_16_006())
