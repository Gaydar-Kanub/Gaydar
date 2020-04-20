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
# c = ''.join(filter(lambda x: s.index(x) in ind, s))       # подходит при условии не повторяющихся символов
# print(c)

# Slide 5 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# s = 'sdfDSdfsSdf, sdVGD. EFfdd. dfEFR dsfFD.'
# s = '. '.join(map(lambda x: x[0].upper() + x[1:].lower(), s.split('. ')))
# print(s)

# Slide 6 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#
import math
from functools import reduce

# items = [1, 24, 17, 14, 9, 32, 2]
# all_max = reduce(lambda a, b: a if (a > b) else b, items)
# print(all_max)


# for_fibonachi = [i for i in range(10)]                # Это так, для себя
# print(reduce(lambda x, y: x + y, for_fibonachi))



def pipeline_each(x, funcs):
    for func in funcs:
        x = func(x)
    return x


f = [math.cos, math.sin, math.tan]
a = it.count(0.1, 0.01)
# a = 0.5
for _ in range(5):
    b = next(a)
    print(math.tan(math.sin(math.cos(b)))     )         # for check
    print('======================')
    print(reduce(lambda x, y: y(x), [b] + f))
# print(pipeline_each(next(a), f))

