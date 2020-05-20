# import random
# random.seed(7)
#
# a = list(map(lambda x, y: (x, y), [random.randint(-10, 10) for _ in range(5)], [random.randint(-10, 10) for _ in range(5)]))
# print(a)
# a = sorted(a, key=lambda x: x[1], reverse=1)
# print(a)
#
#
#
# a = [(random.randint(-10, 10), random.randint(-10, 10)) for _ in range(5)]
# print(a)
# a = sorted(a, key=lambda x: x[1], reverse=1)
# print(a)
#
#
#
#
# # b = ['hello', ' happy', 'word', 'thunder', 'hell', 'a']
# b = [''.join(chr(random.randint(97, 122)) for _ in range(random.randint(1,10))) for _ in range(8)]
# b = sorted(b, key=lambda x: len(x), reverse=1)
# print(b)
#
# p = 15
# c = list(map(lambda x: x+p, [i for i in range(10)]))
# print(c)
# c = lambda x: lambda y: x + y
#
# print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
#
# d = "Two roads diverged in a yellow wood," \
#     "And sorry I could not travel both" \
#     "And be one traveler, long I stood" \
#     "And looked down one as far as I could" \
#     "To where it bent in the undergrowth."
#
#
# def words(text):
#     i = 0
#     while True:
#         yield d.split(' ')[i]
#         i += 1
#
#
# q = words(d)
# for _ in range(len(d.split(' '))):
#     print(next(q))
# print(next(words(d)))
#
# # def f(s):
# #     for i in s.split(' '):
# #         yield i
#
# print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
#
#
# import time
# # e = map(lambda x: 4 ** (int(str(time.time())[-5:-2]) / 3 + 1), [i for i in range(10)])
# # print(list(e))
#
#
# def ffsh(t=None):
#     while True:
#         if t is None:
#             x = time.time()
#         else:
#             x = t
#         u = int(str(4 ** (int(str(x)[-5:-2]) / 300 + 1))[-(int(str(x)[-1])+1):])
#         yield u
#
#
# # w = ffsh(100)
# w = ffsh()
# for _ in range(7):
#     print(next(w))
# print(next(w))
# print(next(w))
#
# print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
#

# def cor(start=3):
#       num = start
#       while True:
#             new_start = yield num
#             if new_start is not None:
#                 num = new_start + 1
#             else:
#                 num += 1
#
#
# f = cor(4)
# print(next(f))
# next(f)
# print(next(f))
# print(f.send(30))
# # print(f.send(None))
# print(next(f))
#
#
# print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
# print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
# print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
#

# def dec1(f):
#     def inner(*ar, **kw):
#         r = f(*ar, **kw)
#         inner.kolvo += 1
#         print('Вызвано', inner.kolvo, 'раз')
#         return r
#     inner.kolvo = 0
#     return inner
#
#
# @dec1
# def incr(n):
#     return n + 1
#
#
# @dec1
# def summ(a, b):
#     return a + b
#
#
# incr(1)
# incr(1)
# incr(1)
# summ(2, 3)
# incr(1)
# summ(1, 1)


# import datetime
# import time
# import math
#
#
# # def my_dec(e):
# #     def wrapper(*ar, **kw):
# #         if ar in wrapper.cashe:
# #             res = wrapper.cashe[ar]
# #         else:
# #             res = e(*ar, **kw)
# #             wrapper.cashe[ar] = res
# #         return res
# #     wrapper.cashe = {}
# #     return wrapper
#
#
# def my_dec(e):
#     def wrapper(*ar, **kw):
#         ar_kw = str(ar) + ' ' + str(kw)
#         if ar_kw in wrapper.cashe:
#             res = wrapper.cashe[ar_kw]
#         else:
#             res = e(*ar, **kw)
#             wrapper.cashe[ar_kw] = res
#         return res
#     wrapper.cashe = {}
#     return wrapper
#
#
# def taymer(e):
#     def wrapper(*arg, **kwa):
#         start = datetime.datetime.now()
#         res = e(*arg, **kwa)
#         print(datetime.datetime.now() - start)
#         return res
#     return wrapper
#
#
# @taymer
# @my_dec
# def example(n, x):
#     time.sleep(2)
#     return math.sqrt((n * x) ** 2)
#
#
# @my_dec
# def example22(n, x):
#     time.sleep(1)
#     return n + x
#
#
# # start = datetime.datetime.now()
# # print(example(3333, 54444))
# # print(datetime.datetime.now() - start)
# # start = datetime.datetime.now()
# # print(example22(3333, 54444))
# # print(datetime.datetime.now() - start)
# # start = datetime.datetime.now()
# # print(example(3333, 54444))
# # print(datetime.datetime.now() - start)
# # start = datetime.datetime.now()
# # print(example22(3333, 54444))
# # print(datetime.datetime.now() - start)
#
#
# for i in range(10):
#     example(3333, 54444)


# print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
# print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
# print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

# 1 - декоратор и 2 функции
# import datetime as dt
# import time
# time.t
#
# def my_dec(func):
#     def wrapper(*ar, **kw):
#         if ar in wrapper.cash:
#             res = wrapper.cash[ar]
#         else:
#             res = func(*ar, **kw)
#             wrapper.cash.append(res)
#         return res
#     wrapper.cash = []
#     return wrapper
#
#
# def timer(func):
#     def wrapper(*arg, **kwa):
#         start = dt.datetime.now()
#         res = func(*arg, **kwa)
#         print(dt.datetime.now() - start)
#         return res
#     return wrapper
#
#
# @timer
# @my_dec
# def fibonachi_naiv(n):
#     a, b = 0, 1
#     if n == 0 or n == 1:
#         b = n
#     else:
#         while n - 2 > 0:
#             a, b = b, a + b
#             n -= 1
#     return b
#
#
# @my_dec
# @timer
# def fibonachi_cashe(n):
#     a, b = 0, 1
#     res = []
#     if n > 0:
#         res.append(a)
#     if n > 1:
#         res.append(b)
#     while n - 2 > 0:
#         a, b = b, a + b
#         n -= 1
#         res.append(b)
#     return res
#
#
# print(fibonachi_naiv(80))
# print(fibonachi_cashe(80))
# print(fibonachi_cashe.cashe)


# print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
# print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
# print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
