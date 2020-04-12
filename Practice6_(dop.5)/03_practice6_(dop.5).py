# 1
# def exponent2_001(num):
#     res = 'Нет, это число не является степенью 2'
#     while num > 0:
#         if num == 1:
#             res = 'Да, это число является степенью 2'
#             break
#         elif num % 2 == 0:
#             num = num // 2
#         else:
#             break
#     return res
#
#
# print(exponent2_001(18))
# print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

# 2
# def sum_nums_002(num):
#     s = 0
#     while num > 0:
#         s += num % 10
#         num = num // 10
#     return s
#
#
# a = 123456
# print(sum_nums_002(a))
# print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')


# 3
# def sum_nums_003(num):
#     s = 0
#     while num > 0:
#         if num % 2 == 0:
#             s += num % 10
#         num = num // 10
#     return s
#
#
# a = 123456
# print(sum_nums_003(a))
# print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')


# 4
# def num_max_004(a):
#     num = 0
#     for i in str(a):
#         if int(i) > num:
#             num = int(i)
#     return num
#
#
# a = 123456
# print(num_max_004(a))
# print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')


# 5
# def sim_sum_005(nums):
#     res = []
#     for num in nums:
#         if sum(map(int, list(str(num)[:3]))) == sum(map(int, list(str(num)[3:]))):
#             res.append(num)
#     return res
#
#
# l = [i for i in range(100000, 1000000)]
# print(sim_sum_005(l))
# print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')


# 6
# def max_denom(A, B):
#     num = min(A, B)
#     res = 'У чисел А и В нет общего делителя'
#     while num > 0:
#         if A % num == 0 and B % num == 0:
#             res = f'Наивольший делитель чисел A и B = {num}'
#             break
#         else:
#             num -= 1
#     return res

#
# a,b = 25, 45
# print(max_denom(a, b))