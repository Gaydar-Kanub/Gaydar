# Гайдаренко Евгений Григорьевич


# for num in range(99, 0, -1):
#     print(f'{num} bottles of beer on the wall')
#     print(f'{num} bottles of beer!')
#     print('Take one down, pass it around')
#     print(f'{num - 1} bottles of beer on the wall!')


# def multiplic():
#     for i in range(9):
#         for j in range(9):
#             print(f'{i} * {j} = {i * j}')
#         print('')
#     return ''

# print(multiplic())


# import random

# def even_(numbers):
#     count = 0
#     for num in numbers:
#         if num % 2 != 0:
#             count += 1
#     return count


# l = [random.randint(0, 15) for _ in range(9)]
# print(l)
# print(even_(l))


# l = [chr(i) for i in range(256)]

# print(l)


# def a2(num):
#     while num != 1:
#         if num % 2 == 0:
#             num = num % 2
#         else:
#             return 'Это число не является степенью 2'
#     return 'Это число является степенью 2'

# print(a2(16))


# 2
a = 123456

# def nums(n):
#     s = 0
#     while n > 0:
#         s += n % 10
#         n = n // 10
#     return s
# print(nums(a))

# Спасибо !!

# # 3
# def nums(n):
#     s = 0
#     while n > 0:
#         if n % 2 == 0:
#             s += n % 10
#         n = n // 10
#     return s


# print(nums(a))


# # 4
# def num_max(a):
#     nm = 0
#     for i in str(a):
#         if int(i) > nm:
#             nm = int(i)
#     return nm


# print(num_max(a))


# # 5
# l = [i for i in range(100000, 1000000)]


# def sim_sum(nums):
#     res = []
#     for num in nums:
#         if int(str(num)[0]) + int(str(num)[1]) + int(str(num)[2]) == int(str(num)[3]) + int(str(num)[4]) + int(str(num)[5]):
#             res.append(num)
#     return res


# print(sim_sum(l))


#6

# Генераторы !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# 1
# n,m = 43,54
# l = [1 / i for i in range(1, 100000) if i % n == 0 or i % m == 0]
# print(l)


# 2
d = {chr(i): chr(i).capitalize() for i in range(97, 123)}
print(d)


# 3
def gen_100(n=5, m=7):
    return [i for i in range(1, 1000) if i % n == 0 or i % m == 0]
print(gen_100())


# 4
def divide(num):
    n = 2
    res = []
    while num > 1:
        if num % n == 0:
            res.append(n)
            num = num // n
            continue
        else:
            n += 1
    return res

print(divide(10080))

n = 10080
l = [i for i in range(2, n) if n % i == 0]
print(l)

# 5


