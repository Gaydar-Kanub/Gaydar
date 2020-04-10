import numpy as np


# 1
matrix1 = np.eye(7) * 5
print(matrix1)


# 2
matrix2 = np.random.randint(-20, 20, (7, 7))
print(matrix1 * matrix2)


# 3
print(matrix2 @ matrix1)


# 4
array = np.random.randint(-100, 100, 100)
print(array)
midle = []
for i in range(2, len(array) - 2):
    midle.append((array[i-2] + array[i-1] + array[i] + array[i+1] + array[i+2]) / 5)
print(midle)
