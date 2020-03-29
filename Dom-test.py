#SOSTAVNIE TYPI

#a = input()


#1
# for i in range(1, (int(a) + 1)):
#     print('*' * i)

#2
# a = 'мою мою яму'
# b = ''
# for i in set(a):
#     if 'А' <= i <= 'я':
#         b += i + ' - ' + str(a.count(i)) + ' шт, '
# print(b)

#3
a = 'ем ем ем я ем ем суп три дня'
a = a.split(' ')
b = {}
c = ''
for i in a:
    if f'длинной {len(i)}' in b:
        b[f'длинной {len(i)}'] += 1
    else:
        b[f'длинной {len(i)}'] =  1
# print((f'{i.ke} - {b[i]} шт') for i in sorted(b.items(), reverse = True))
for i in sorted(b.keys(), reverse = True):
    c += f'{i} - {b[i]} шт, '
print(c)

    # print(type(i), i, b[i])
# for i in range(len(b),0,-1):
