# import itertools
#
# def mk_dec_lang(arg):
#     dictionary = {'ru': ('Функция выполнялась', 'сек'),
#                   'en': ('Function performed', 'sec')}
#     lang = dictionary[arg]
#     def my_dec_timer(func):
#         def wr(*args):
#             import time
#             start = time.time()
#             time.sleep(1)
#             res = func(*args)
#             stop = time.time()
#             print(f'{lang[0]}: {stop - start} {lang[1]}.')
#             return res
#         return wr
#     return my_dec_timer
#
#
# @mk_dec_lang('en')
# def s2(y):
#     return y ** 2
#
# a = map(s2,  filter(lambda x: x % 2 == 0, itertools.count(1, 1)))
#
# for _ in range(10):
#     print(next(a))

# print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
# Практика №1
# import itertools as it
#
#
# def pow_2(x):
#     return x ** 2
#
#
# a = map(pow_2, filter(lambda x: x % 2 == 0, it.count(0, 1)))
# for _ in range(10):
#     print(next(a))
#
# print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
#
# line = 'Всем привет'
# roster = [1, 3, 5]
#
# print(''.join(filter(lambda x: line.index(x) in roster, line)))
# print(''.join(line[i] for i in roster))
# print(''.join(map(lambda x: line[x], roster)))
#
# print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
#
# line = 'sdfDSdfsSdf, sdVGD. EFfdd. dfEFR dsfFD.'
# print('. '.join(map(lambda x: x[0].upper() + x[1:].lower(), line.split('. '))))
#
# print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
#
# from functools import reduce
#
#
# def pipeline_each(x):
#     return  x * 2
#
#
# a = map(pipeline_each, it.count())
# for _ in range(10):
#     print(next(a))
# print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
#
# import math
#
# items = [1, 24, 17, 14, 9, 32, 2]
# all_max = reduce(lambda x, y: x if (x > y) else y, items)
# print(all_max)
#
#
# def pipeline_each(x, funcs):
#     for func in funcs:
#         x = func(x)
#     return x
#
#
# f = [math.cos, math.sin, math.tan]
# a = it.count(0.1, 0.01)
# # a = 0.5
# for _ in range(5):
#     b = next(a)
#     print(math.tan(math.sin(math.cos(b))))         # for check
#     print(reduce(lambda x, y: y(x), [b] + f))
#     print(pipeline_each(b, f))
#     print('======================')

# print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
# print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
# print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

# Практика №2

# import random
#
# roster = list(map(lambda x, y: (x, y), [random.randint(0, 20) for _ in range(10)],
#                   [random.randint(0, 20) for _ in range(10)]))
# print(roster)
# roster = sorted(roster, key=lambda x: x[1], reverse=1)
# print(roster)
# roster = [''.join(chr(random.randint(ord('a'), ord('z'))) for _ in range(random.randint(2, 10))) for _ in range(10)]
# roster = sorted(roster, key=lambda x: len(x), reverse=1)
# print(roster)
# r = list(map(lambda x: lambda y: y + x, roster))

# d = "Two roads diverged in a yellow wood," \
#     "And sorry I could not travel both" \
#     "And be one traveler, long I stood" \
#     "And looked down one as far as I could" \
#     "To where it bent in the undergrowth."
#
#
# def word_from_sentence(text):
#     i = 0
#     start = 0
#     while i < len(text):
#         if not text[i].isalpha():
#             res = text[start:i]
#             start = i + 1
#             if res.isalpha():
#                 yield res
#         i += 1
#
#
# a = word_from_sentence(d)
# for _ in range(20):
#     print(next(a))

# import time
# import math
# t = time.time()
# print(t)
# e = map(lambda x: (int(str(time.time())[-5:-2]) / (3 * x - 1) + 1), [i for i in range(10)])
# print(list(e))
#
#
# def ffsh(t=None):
#     i = 0
#     while True:
#         if t is None:
#             t = time.time()
#         res = int(str(t)[-5:-2]) / (3 * i - 1) + 1
#         i += 1
#         yield res
#
#
# num = ffsh(54276854320)
# for _ in range(10):
#     print(next(num))

# def my_increment(start=0):
#     while True:
#         new_start = yield start
#         if new_start is not None:
#             start = new_start
#         else:
#             start += 1
#
# q = my_increment(3)
# # q.send(None)
# # q.send(None)
# # q.send(None)
# for _ in range(4):
#     print(next(q))
# print(q.send(30))
# for _ in range(10):
#     print(next(q))
#
# print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

# import itertools
# import datetime as dt
# import time
#
#
# def my_dec_timer(func):
#     def wr(*args):
#         start = time.time()
#         time.sleep(1)
#         print(f'Function was started at {dt.datetime.now()}')
#         res = func(*args)
#         stop = time.time()
#         wr.kol_vo += 1
#         print(f'Функция выполнялась: {stop - start} сек.')
#         print(f'Function started {wr.kol_vo} times')
#         return res
#     wr.kol_vo = 0
#     return wr
#
#
# def my_dec_2(func):
#     def envelop(*args):
#         if args in envelop.args:
#             res = envelop.res[args]
#         else:
#             res = func(*args)
#             envelop.res[args] = res
#             envelop.args.append(args)
#         return res
#     envelop.args = []
#     envelop.res = {}
#     return envelop
#
#
# @my_dec_2
# def ss2(y):
#     time.sleep(1)
#     return y ** 2
#
#
# @my_dec_2
# def s2(y):
#     time.sleep(1)
#     return y * 2
#
#
# a = map(s2, [1, 2, 3, 4, 1, 2, 1, 2, 3, 8])
# b = map(ss2, [1, 2, 3, 4, 1, 2, 1, 2, 3, 8])
# for _ in range(10):
#     print(next(a))
# print(s2.res)
# print(s2.args)
# for _ in range(10):
#     print(next(b))
# print(ss2.res)
# print(ss2.args)
# print(s2.res)
# print(s2.args)

# import time
# #
# #
# # def my_dec(func):
# #     def envelop(*args):
# #         res = func(*args)
# #         envelop.t = time.time() - envelop.t
# #         return res
# #     envelop.t = time.time()
# #     return envelop
# #
# #
# # def my_dec_cash(func):
# #     def inner(arg):
# #         while inner.step <= arg:
# #             res = func(inner.step)
# #             inner.cash[inner.step] = res
# #             inner.step += 1
# #         inner.t = time.time() - inner.t
# #         return res
# #     inner.step = 0
# #     inner.cash = {}
# #     inner.t = time.time()
# #     return inner
# #
# #
# # @my_dec
# # def fibonachi(x=0):
# #     a, b = 0, 1
# #     if x == 0 or x == 1:
# #         b = x
# #     i = 2
# #     while i <= x:
# #         a, b = b, a+b
# #         i += 1
# #     return b
# #
# #
# # @my_dec_cash
# # def fibonachi_cash(x=0):
# #     a, b = 0, 1
# #     if x == 0 or x == 1:
# #         b = x
# #     i = 2
# #     while i <= x:
# #         a, b = b, a + b
# #         i += 1
# #     return b
# #
# #
# #
# # print(fibonachi(5000))
# # print(fibonachi.t)
# # print(fibonachi_cash(5000))
# # # print(fibonachi_cash.cash)
# # print(fibonachi_cash.t)
# # # print(fibonachi_cash.t)

# print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
# print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
# print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

import os
import json
import pickle

# path = os.getcwd()
# print(os.path.dirname(path))
# path = os.path.join(os.getcwd(), 'tmp')
# # path = os.path.join(path, 'text.txt')
# print(path)
# print(os.path.basename(path))

# with open('text_pr3.txt', 'w') as file:
#     print("Введите некоторую информацию для записи в файл: ")
#     file.write(input())
#
# with open('text_pr3.txt', 'rb') as file:
#     print(file.read())

# a = os.environ
# dictionary = {0: {1: 'тест', 2: 'world', 3: 'щука', 4: 'gastropub', 5: 'феникс'}, 6: ['aaa', 'sss', 'ddd', 'fff']}
# a = json.dumps(dictionary, indent='\t')
# print(a)
# b = json.loads(a)
# print(b)
# with open('text_pr3.txt', 'w') as file:
#     json.dump(dictionary, file, indent='\t')
#     # file.write(a)

# a = os.environ
# # a = json.dumps(a, indent=1)
# if 'PY_DEBUG' in a and a['PY_DEBUG'] == 'True':
#     # print(json.dumps(dict(a), indent='\t'))
#     for x in a:
#         print(x)
#         print('\t' + a[x].replace(';', '\n\t'))

# print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
# print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
# print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

