# def get_pow(n):
#     def pow_(a):
#         return a ** n
#     return pow_
#
# pow_2 = get_pow(2)
#
# print(pow_2(5))
# print(get_pow(2)(5))

print('=====================================================')
# import time
#
#
# def decorator_time(fn):
#     def wrapper():
#         print(f'Запустилась функция {fn}')
#         t0 = time.time()
#         result = fn()
#         dt = time.time() - t0
#         print(f'Функция выполнилась. Время {dt:.40f}')
#         return result
#     return wrapper
#
#
# @decorator_time
# def pow_2():
#     return 1000000 ** 10000
#
#
# @decorator_time
# def in_build_pow():
#     return pow(1000000, 10000)
#
# # pow_2 = decorator_time(pow_2)
# # in_build_pow = decorator_time(in_build_pow)
#
#
# print(pow_2())
# in_build_pow()

print('=====================================================')

#
# def my_decorator(a_function_to_decorate):
#     # Здесь мы определяем новую функцию – «обертку». Она нам нужна, чтобы выполнять
#     # каждый раз при вызове оригинальной функции, а не только один раз
#     def wrapper():
#         # здесь поместим код, которые будет выполняться до вызова, потом вызов
#         # оригинальной функции, потом код после вызова
#         print("Я буду выполнен до основного вызова!")
#
#         result = a_function_to_decorate()  # не забываем вернуть значение исходной функции
#
#         print("Я буду выполнен после основного вызова!")
#         return result
#
#     return wrapper
#
#
# @my_decorator
# def my_function():
#     print("Я – оборачиваемая функция!")
#     return 0
#
#
# my_function()


# def type_checker(tipi):
#     def decor(func):
#         def wrapper(*args, **kwargs):
#             if type(*args) == tipi:
#                 result = func(*args, **kwargs)
#                 return result
#         return wrapper
#     return decor
#
#
# @type_checker(int)
# def pretty_fun(x):
#     print(x)
#     return x
#
#
# pretty_fun(3)
# pretty_fun("xxx")
