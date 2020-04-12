# 1
# n, m = 43, 54
# l = [1 / i for i in range(1, 1000) if i % n == 0 or i % m == 0]
# print(l)


# 2
# d = {chr(i): chr(i - (ord('a') - ord('A'))) for i in range(ord('a'), ord('z') + 1)}
# print(d)


# # 3
# def gen_100_003(n=5, m=7):
#     return [i for i in range(1, 1000) if i % n == 0 or i % m == 0]
#
#
# print(gen_100_003())


# # 4
# def divide_004(num):
#     res = [i for i in range(1, num // 2 + 1) if num % i == 0]
#     return res
#
#
# print(divide_004(100))


# 5
# def roster_005():
#     res = [i for i in range(1000, 10000) if len(set(str(i))) == 4]
#     return res
#
#
# print(roster_005())
