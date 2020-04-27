import numpy as np
from matplotlib import pyplot as plt


# 1 - гистограмма
# array = np.random.randint(0, 10, 100)
# plt.hist(array)
# plt.show()


# 2 - кругвая диаграмма
# array = np.random.randint(1, 10, 5)
# print(array)
# plt.pie(array)
# plt.show()


# 3 - график
# x = np.arange(0,100)
# print(x)
# y = x ** 3
# print(y)
# # plt.plot(x, y)
# # plt.show()


# 4
# def visual_func_004(x):
#     plt.plot(x, x + x ** 2 - 5)
#     plt.plot(x, 1 / x)
#     plt.plot(x, x / (1 + abs(x)))
#     plt.show()
#
#
# array = np.arange(-10, 10)
# visual_func_004(array)


# 5
x = np.arange(0.01, 1, 0.01)
print(x)


plt.plot(x, np.cos(x))
plt.show()
print('cos')


plt.plot(x, np.sin(x))
plt.show()
print('sin')


plt.plot(x, np.tan(x))
plt.show()
print('tg')


plt.plot(x, 1 / np.tan(x))
plt.show()
print('ctg')




