# import itertools
#
# def s2(y):
#     return y ** 2
#
# a = map(s2,  filter(lambda x: x % 2 == 0, itertools.count(1, 1)))
#
# for _ in range(10):
#     print(next(a))
#
#
# i = [1, 3, 5]
# q = 'Всем привет'
# s = ''
# for j in i:
#     s += q[j]
# print(s)

# s = ''.join(q[j] for j in i)
# s = filter(lambda x: q.index(x) in i,q)
# print(list(s))
# print(''.join(s))
# print(list(map((lambda x: q[x], i))))

# r = ''
# w = (r + q[e] for e in i)
# for _ in range(len(i)):
#     r = next(w)
# print(r)

