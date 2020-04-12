from matplotlib import pyplot as plt


way = r'D:\\'
file = open(way + 'data.txt', 'r')
text = file.read()
file.close()
# print(text)


# 1
# print(len(text))
# # 2
# print(len(set(text)))
# 3


def top_10_001_3(symbols):
    dic_sym = {}
    for sym in set(symbols):
        dic_sym[sym] = text.count(sym)
    top = list(dic_sym.items())
    top.sort(key=val_sort_003, reverse=True)
    return top[0:10]


def val_sort_003(val):
    return val[1]


# print(top_10_001_3(text))
# x = ''
# for i in top_10_001_3(text):
#     x += i[0] * i[1]
# plt.hist(list(x))
# plt.show()


print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')


import datetime as dt


a = dt.datetime.now()
# b = dt.date()
print(a)
# print(b)