# file = open('prac3.txt', 'w')
# print('Введите сообщение для записи в файл.')
# file.write(input())
# file.close()
#
# with open('prac3.txt', 'br') as file:
#     print(file.read())


# import json
#
# dictionary = {0: {1: 'тест', 2: 'world', 3: 'щука', 4: 'gastropub', 5: 'феникс'}, 6: ['aaa', 'sss', 'ddd', 'fff']}
#
# with open('prac3_slide3.txt', 'w') as file:
#     a = json.dumps(dictionary, indent='\t')
#     file.write(a)
#     # print(a)
#     # print(json.loads(a))

# import pickle
#
# dictionary = {0: {1: 'тест', 2: 'world', 3: 'щука', 4: 'gastropub', 5: 'феникс'}, 6: ['aaa', 'sss', 'ddd', 'fff']}
# with open('prac3_slide4.txt', 'bw') as file:
#     pickle.dump(dictionary, file)
#
# with open('prac3_slide4.txt', 'br') as file:
#     print(pickle.load(file))

# import json
# import os
#
# a = os.environ
# if 'PY_DEBUG' in a and a['PY_DEBUG'] == 'True':
#     print(json.dumps(dict(a), indent='\t'))     # 1 Вариант
#     for i in a:                                 # 2 Вариант
#         print(i)
#         print('\t', a[i].replace(';', '\n \t'))

# import sys
# import os
#
# ar = sys.argv
# print(ar)
#
# # Мой вариант
# if len(ar) > 1:
#     if os.path.exists(os.path.join(ar[1], ar[2])):
#         print("Такой файл в этой директории уже существует")
#     else:
#         print('All Ok.')
#         with open(os.path.join(ar[1], ar[2]), 'w') as file:
#             file.write('All Ok.')
#
# # Вариант препода
# if os.path.exists(os.path.join(ar[1], ar[2])) and os.access(os.path.join(ar[1], ar[2]), os.W_OK):
#     try:
#         f = open(os.path.join(ar[1], ar[2]), 'w')
#         f.close()
#         os.remove(os.path.join(ar[1], ar[2]))
#     except:
#         print(False)
#     else:
#         print(True)

# print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
# print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
# print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
import pandas as pd

# d = pd.read_excel('book.xlsx')
# print(d)            # первую строку он воспринимает как заголовки(шапку) таблицы
# print(d['fdg'])     # вызов столбца с заголовком 'fdg'
# d.to_csv('file.csv', sep="\t")


# import numpy as np
# dd = np.genfromtxt('file.csv', delimiter='\t')
# print(dd)
# print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
# print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
# print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
#
# from PIL import Image
# import numpy as np
# from matplotlib import pyplot as plt
#
# jpg = Image.open('for_python.jpg')
# jpg2 = Image.open('for_python2.jpg')
# arr = np.asarray(jpg)
# arr2 = np.asarray(jpg2)
# print(arr)
# print(arr.shape)
# print(arr2)
# print(arr2.shape)
# plt.imshow(arr[:, :, 2])
# plt.show()
# plt.imshow(arr2[:, :, 2])
# plt.show()

# print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
#
#
# import random
#
# # la = 'ru'
# la = 'en'
#
#
# def lang_dec_fab(lang):
#     base = {'ru': ['стартует', 'закончила свое выполнение'],
#             'en': ['start', 'finish']}
#
#     def dec(func):
#         def wrapper(*args):
#             print(f'{func.__name__} {base[lang][0]}')
#             res = func(*args)
#             print(f'{func.__name__} {base[lang][1]}')
#             return res
#         return wrapper
#     return dec
#
#
# @lang_dec_fab(la)
# # @dec
# def get_number():
#     x = -1
#     while not 1 <= x <= 100:
#         x = ''
#         while not x.isdigit():
#             x = input("Введите число:\n")
#         x = int(x)
#     return x
#
#
# @lang_dec_fab(la)
# # @dec
# def step(n):
#     x = get_number()
#     if x > n:
#         print("Мое меньше!")
#         return False
#     elif x < n:
#         print("Мое больше!")
#         return False
#     else:
#         print("Победа!")
#         return True
#
#
# @lang_dec_fab(la)
# # @dec
# def single_game():
#     n = random.randint(1,100)
#     win = False
#     while not win:
#         win = step(n)
#
#
# @lang_dec_fab(la)
# # @dec
# def game():
#     ans = "y"
#     while ans == "y":
#         single_game()
#         ans = input("Хотите сыграть еще?")
#         if ans.lower() in ("да", "конечно", "yes", 'y'):
#             ans = "y"
#
#
# g = game()
