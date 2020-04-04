# Хотелось бы импортировать раннее написанные функции из предыдущего слайда, но не получается из-за названия файла
# from Practice4.practice_04 import num_sys_16_10_002 - а вот так можно было бы (файл не начинается с цифр)


def num_sys_8_10_001(octets=None):
    if octets is None:
        print('Введите число для перевода его из восьмеричной сист.счисления в десятеричную сист.счисления')
        octets = input()
    dec = 0
    for i in range(len(octets)):
        dec += int(octets[-i-1]) * 8 ** i
    return dec


def num_sys_10_16_001(dec=None):
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


def num_sys_8_16_001():
    print('Введите число для перевода его из восьмеричной сист.счисления в шестнадцатиричную сист.счисления')
    octets = input()
    dec = num_sys_8_10_001(octets)
    hexa = num_sys_10_16_001(dec)
    return hexa


# print(num_sys_8_16_001())


def num_sys_16_10_002(hexa=None):
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


def num_sys_10_8_002(dec=None):
    if dec is None:
        print('Введите число для перевода его из десятеричной сист.счисления в восьмеричную сист.счисления')
        dec = int(input())
    octets = ''
    if dec == 0:
        return '0'
    while dec > 0:
        octets += str(dec % 8)
        dec = dec // 8
    return octets[::-1]


def num_sys_16_8_002():
    print('Введите число для перевода его из шестнадцатиричной сист.счисления в восьмеричную сист.счисления')
    hexa = input()
    dec = num_sys_16_10_002(hexa)
    octets = num_sys_10_8_002(dec)
    return octets


# print(num_sys_16_8_002())


def num_sys_10_7_003(dec=None):
    if dec is None:
        print('Введите число для перевода его из десятеричной сист.счисления в семеричную сист.счисления')
        dec = int(input())
    seven = ''
    if dec == 0:
        return '0'
    while dec > 0:
        seven += str(dec % 7)
        dec = dec // 7
    return seven[::-1]


# print(num_sys_10_7_003())


def num_sys_7_10_004(seven=None):
    if seven is None:
        print('Введите число для перевода его из семеричной сист.счисления в десятеричную сист.счисления')
        seven = input()
    dec = 0
    for i in range(len(seven)):
        dec += int(seven[-i-1]) * 7 ** i
    return dec

# print(num_sys_7_10_004())


def num_sys_10_3_005(dec=None):
    if dec is None:
        print('Введите число для перевода его из десятеричной сист.счисления в троичную сист.счисления')
        dec = int(input())
    three = ''
    if dec == 0:
        return '0'
    while dec > 0:
        three += str(dec % 3)
        dec = dec // 3
    return three[::-1]


# print(num_sys_10_3_005())


def num_sys_3_10_006(three=None):
    if three is None:
        print('Введите число для перевода его из троичной сист.счисления в десятеричную сист.счисления')
        three = input()
    dec = 0
    for i in range(len(three)):
        dec += int(three[-i-1]) * 3 ** i
    return dec


# print(num_sys_3_10_006())


def num_sys_3_7_007():
    print('Введите число для перевода его из троичной сист.счисления в семеричную сист.счисления')
    three = input()
    dec = num_sys_3_10_006(three)
    seven = num_sys_10_7_003(dec)
    return seven


# print(num_sys_3_7_007())


def num_sys_7_3_008():
    print('Введите число для перевода его из семеричной сист.счисления в троичную сист.счисления')
    seven = input()
    dec = num_sys_7_10_004(seven)
    three = num_sys_10_3_005(dec)
    return three


# print(num_sys_7_3_008())