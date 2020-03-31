# a = int(input())
# print(a *6)

# n = input()
# s = input()
# print(int(n) * (s + '\n'))

# N = int(input())
# for i in range(1, N + 1):
#     print('*' * i)

# мою мою яму


# string = input()
# b = {}
# for i in string:
#     if i in b:
#         b[i] += 1
#     else:
#         b[i] = 1
# for i in b:
#     print(f'{i} - {b[i]} штуки')

# string = input()
# b = {}
# for i in set(string):
#     if 'а' <= i <= 'я':
#         b[i] = string.count(i)
# for i in b:
#     print(f'{i} - {b[i]} штуки')


fullname = 'Гайдаренко Евгений'
N = (len(fullname.split(' ')[0]) + len(fullname.split(' ')[1]))% 5
l=[i for i in range((N+2)*2)]
print(l)

# l = [0, 6, 3, 4, 5, 6, 7]
# l = l[l.index(sorted(set(l))[-2]):-1]
# print(l)

l = l + [(i + 1) for i in l]
print(l)

l = [i for i in l if i % 3 == 1]
print(l)


# l = [round(l[i] / 3) for i in range(len(l))]
# print(l)




