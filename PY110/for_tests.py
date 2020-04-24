# def grep(pattern):
#     i = 0
#     while True:
#         line = yield
#         if pattern in line:
#             i += 1
#             print(f'Found, overall: {i}')
#
#
# g = grep('python')
# next(g)
# # g.send(None)
# g.send('some string here python')
# g.send('some string here ')
# g.send('some  here python')
# g.send('some string  python')
#
#
# def counter(start):
#     n = start
#     while True:
#         new_start = yield n
#         if new_start is not None:
#             n = new_start
#         else:
#             n += 1
#
#
# c = counter(3)
# for _ in range(10):
#     next(c)
# print(c.send(57))
# print(c.send(None))
# print(next(c))

print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

# def strange_fun():
#     for i in range(5):
#         yield 0
#     while True:
#         yield 1
#
#
# a = strange_fun()
# for _ in strange_fun():
#     print(next(a), end="")
print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

# def strange_fun():
#     for i in range(3):
#         yield 0
#     for i in range(3):
#         yield 1
#
# a = strange_fun()
#
# for _ in range(9):
#     print(next(a))
print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

#
# def my_decorator(fff):
#     print('Начало декоратора - выполняется один раз!!!')
#
#     def wrapper():
#         print('Я буду выполнен до основного вызова!')
#         result = fff()
#         print('Я буду выполнен после основного вызова!')
#         return result
#
#     return wrapper
#
#
# @my_decorator
# def my_function():
#     print('Я оборачиваемая функция!')
#     return 0
#
#
# my_function()
# my_function()
# my_function()
#
# print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
#
#
# def do_it_twice(func):
#     def wrapper():
#         func()
#         func()
#     return wrapper
#
#
# @do_it_twice
# def say_whee():
#     print('Whee!')
#
# # say_whee = do_it_twice(say_whee)
#
# say_whee()
# say_whee()
# say_whee()