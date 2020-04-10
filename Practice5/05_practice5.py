import numpy as np


# 1 + 5
# array1 = np.random.randint(1, 10, 10)
array1 = np.random.randint(1, 10, 10000)
print(array1)


# 2
array2 = np.random.randint(-5, 20, 10000)
print(array2)


#3
sum_arr = array1 + array2
print(sum_arr)


# 4
midle = 0
for i in sum_arr:
    midle += i
midle = midle / len(sum_arr)
print(midle)
print(np.mean(sum_arr))


# 5
midle1 = np.mean(array1)
print(midle1)
midle2 = np.mean(array2)
print(midle2)
print(midle > midle1)
print(midle > midle2)