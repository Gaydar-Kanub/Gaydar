# file = open('prac3.txt', 'w')
# print('Введите сообщение для записи в файл.')
# file.write(input())
# file.close()
#
# with open('prac3.txt', 'br') as file:
#     print(file.read())


# import json
#
# dictionary = {0: {1: 'тест', 2: 'world', 3: 'щука', 4: 'gastropub', 5: 'феникс'}, 6: ['aaa', 'sss', 'ddd', 'fff']}
#
# with open('prac3_slide3.txt', 'w') as file:
#     a = json.dumps(dictionary)
#     file.write(a)
#     # print(a)
#     # print(json.loads(a))

# import pickle
#
# dictionary = {0: {1: 'тест', 2: 'world', 3: 'щука', 4: 'gastropub', 5: 'феникс'}, 6: ['aaa', 'sss', 'ddd', 'fff']}
# with open('prac3_slide4.txt', 'bw') as file:
#     pickle.dump(dictionary, file)
#
# with open('prac3_slide4.txt', 'br') as file:
#     print(pickle.load(file))

# import json
# import os
#
# a = os.environ
# if 'PY_DEBUG' in a:
#     print(json.dumps(dict(a), indent='\t'))

# import sys
# import os
# print(5)
# ar = sys.argv
# print(ar[1] + ar[2])
# if os.path.exists(ar[1] + ar[2]):
#     print("Такой файл в этой директории уже существует")
# else:
#     print('All Ok.')

print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
# import pandas as pd

# d = pd.read_excel('book.xlsx')
# print(d)
# d.to_csv('file.csv', sep="\t")

# import numpy as np
# dd = np.genfromtxt('file.csv', delimiter='\t')
# print(dd)
print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

