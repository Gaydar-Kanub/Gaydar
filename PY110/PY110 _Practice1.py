import itertools as it

# Slide 4 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#
# # map & filter
# a = (map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, it.count(1, 1))))
# for _ in range(12):
#     print(next(a))
#
# # map
# a = map(lambda x: x ** 2, it.count(2, 2))
# for _ in range(12):
#     print(next(a))
#
# # filter
# a = filter(lambda x: x % 2 == 0, it.count(1, 1))
# for _ in range(12):
#     print(next(a))
#
#
# s = 'Всем привет'
# ind = [1, 3, 5]
#
# a = ''.join(map(lambda x: s[x], ind))
# print(a)
#
# b = ''.join(s[i] for i in ind)
# print(b)
#
# c = ''.join(filter(lambda x: s.index(x) in ind, s))
# print(c)

# Slide 5 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# s = 'sdfDSdfsSdf, sdVGD. EFfdd. dfEFR dsfFD.'
# s = '. '.join(map(lambda x: x[0].upper() + x[1:].lower(), s.split('. ')))
# print(s)

# Slide 6 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#
# from functools import reduce
#
# items = [1, 24, 17, 14, 9, 32, 2]
# all_max = reduce(lambda a, b: a if (a > b) else b, items)

# print(all_max)
# reduce(lambda x, y: x + y, it.count())
# a = it.count(1, 1)
# for _ in range(10):
#     print(next(a))

# for_fibonachi = [i for i in range(10)]                # Это так, для себя
# print(reduce(lambda x, y: x + y, for_fibonachi))

# Slide 7 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
import math
from functools import reduce


def pipeline_each(x, funcs):
    for i in funcs:
        x = i(x)
    return x



f = [math.cos, math.sin, math.tan]
# a = it.count(0.1, 0.01)
a = 0.5
print(math.tan(math.sin(math.cos(a))))              # for check
print('======================')
print(reduce(lambda x, y: y(x), [a] + f))
print(pipeline_each(a, f))
# for i in range(50):
#     print(reduce(lambda x, y: y(x), [next(a)] + f))
