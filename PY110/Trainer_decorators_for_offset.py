import math
import sys
import re
import random


# 1.1
def dec_digit(func):
    def inner(*args):
        if all(type(x) == int or type(x) == float for x in args):
            res = func(*args)
        else:
            res = 'Wrong data!!!'
        return res
    return inner

# 2.1
# pow_2 = lambda x: 2 ** x
@dec_digit
def pow_2(x):
    return 2 ** x
print(pow_2(3))
# pow_2 = lambda x: math.log2(x)
# print(pow_2(8))


# 1.2
def dec_num_under_100(func):
    def inner(*args):
        if all(1 <= x <= 100 for x in args):
            res = func(*args)
        else:
            res = 'Out of range!!!'
        return res
    return inner

# 2.2
# pow_3 = lambda x: 3 ** x
@dec_num_under_100
def pow_3(x):
    return 3 ** x
print(pow_3(3))
# pow_3 = lambda x: math.log(x, 3)
# print(pow_3(81))


# 1.3
# Смотри пункт 1.1 - уже сделано

# 2.3
ar = sys.argv
# pow_x = lambda x: int(ar[1]) ** x
def pow_y(x):
    return int(ar[1]) ** x
print(pow_y(3))
# pow_x = lambda x: math.log(x, int(ar[1]))
# print(pow_x(81))


# 1.4
def mk_dec_x_times(times):
    def dec_x_times(func):
        def inner(*args):
            res = 0
            for _ in range(times):
                print('time')
                res += func(*args)
            return res / 5
        return inner
    return dec_x_times

@mk_dec_x_times(2)
def test():
    return random.randint(1, 20)


print(test())


# 1.5
def mk_dec_save_file(path):
    def dec_save(func):
        def inner(*args):
            res = func(*args)
            with open(path, 'w') as file:
                file.write(str(res))
            return res
        return inner
    return dec_save


@mk_dec_save_file(r'JUPYTER\test_1_5.txt')
def test_1_5(n):
    return [random.randint(-10, 50) for x in range(n)]


print(test_1_5(15))


# 1.6
def mkdec_under_times(down=1, up=100):
    def dec_times(func):
        def inner(*args):
            res = up + 1
            while not (down <= res <= up):
                res = func(*args)
            return res
        return inner
    return dec_times

@mkdec_under_times()
def test_1_6(n=30):
    return sum([random.randint(-10, 20) for _ in range(n)])

print(test_1_6())


# 2.4
def sym_3(path):
    with open(path, 'r') as file:
        # file.seek(4)
        # file.read(3)
        a = file.read(3)
        return a
print(sym_3('prac3.txt'))


# 2.5
# def word_from_file(path):
#     i = 0
#     with open(path, 'r') as file:
#         while True:
#             if file.read(1).isalpha():
#                 start = i
#                 while True:
#                     if file.read(1).isalpha():
#                         i += 1
#                     else:
#                         file.seek(start)
#                         return file.read(i - start + 1)
#             else:
#                 i += 1
def word_from_file(path):
    with open(path, 'r') as file:
        res = re.search(r'\w+', file.readline())
        return res[0]
print(word_from_file('prac3.txt'))


# 2.6
def pow_y(x):
    a = int(sys.argv[1])
    my_pow = x
    while True:
        p = yield a ** my_pow
        if p is not None:
            my_pow = p

q = pow_y(4)

print(next(q))
print(next(q))
q.send(6)
print(next(q))


# 2.7
def sym_y(path, n=3):
    while True:
        with open(path, 'r') as file:
            # file.seek(4)
            # file.read(3)
            new_n = yield file.read(n)
            if new_n is not None:
                n = new_n

q = sym_y('prac3.txt')
print(next(q))
print(next(q))
q.send(15)
print(next(q))
print(next(q))
print(next(q))

