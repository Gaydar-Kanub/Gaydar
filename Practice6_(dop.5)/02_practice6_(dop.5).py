# 1
# def bottles_001(nums):
#     for num in range(nums, 0, -1):
#         print(f'{num} bottles of beer on the wall')
#         print(f'{num} bottles of beer!')
#         print('Take one down, pass it around')
#         print(f'{num - 1} bottles of beer on the wall!')
#     return ''
#
#
# print(bottles_001(99))
print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')


# 2
# def multiplic_002():
#     for i in range(1, 10, 3):
#         for j in range(1, 10):
#             print(f'{i} * {j} = {i*j}' + '    ' + f'{i+1} * {j} = {(i+1)*j}' + '    ' + f'{i+1} * {j} = {(i+1)*j}')
#         print('')
#     return ''
#
#
# print(multiplic_002())
print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

# 3
# import random
#
#
# def odd_003(numbers):
#     count = 0
#     for num in numbers:
#         if num % 2 != 0:
#             count += 1
#     return count
#
#
# roster = [random.randint(0, 15) for _ in range(9)]
# print(roster)
# print(odd_003(roster))
print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')


# 4
# def tab_ascii(num):
#     for i in range(0, num, 10):
#         line = ''
#         for j in range(0, 10):
#             line += chr(i+j) + ' ' * 9
#         print(line)
#     return ''
#
#
# print(tab_ascii(2500))
print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')


# 5
def hypothec(credit, percent, years):
    payment = credit * percent / 1200 / (1 - (1 + percent / 1200) ** (-years * 12))
    return payment


print(hypothec(20000000, 12, 0.5))