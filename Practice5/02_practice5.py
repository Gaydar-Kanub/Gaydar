import os

way = r'C:\Users\Evgen\Desktop\Python\\'
print(os.listdir(way))

print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

for i in os.listdir(way):
    print(i)

print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

# for i in os.walk(way):
#     print(i)

print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

# Два варианта решения задачи

# 1

# for i1 in os.listdir(way):
#     if os.path.isdir(way + i1):
#         print(i1)
#         for i2 in os.listdir(way + i1):
#             if os.path.isdir(way + i1 + '\\' + i2):
#                 print(' ' * 4 + i2)
#                 for i3 in os.listdir(way + i1 + '\\' + i2):
#                     if os.path.isdir(way + i1 + '\\' + i2 + '\\' + i3):
#                         print(' ' * 8 + i2)
#                     else:
#                         print('\033[1m' + f"{' ' * 8}{i3} \n", end='\033[0;0m')
#
#             else:
#                 print('\033[1m' + f"{' ' * 4}{i2} \n", end='\033[0;0m')
#     else:
#         print('\033[1m' + f'{i1} \n', end='\033[0;0m')


# 2

def pri_fd(way_in, floor=-1):
    floor += 1
    for i in os.listdir(way_in):
        if os.path.isdir(way_in + '\\' + i):
            print(' ' * 4 * floor + i)
            print(pri_fd(way_in + '\\' + i, floor))
        else:
            print('\033[1m' + f"{' ' * 4 * floor}{i} \n", end='\033[0;0m')
    return ''


pri_fd(way)
