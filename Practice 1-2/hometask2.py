"""
For и range, которые мы изучили
в предыдущем файле, можно использовать
для обращения к элементам списка
по индексам. 
Немного про списки и индексы
l = [6,2,5,6,2,1,9] такие индексы
     0 1 2 3 4 5 6
Если мы хотим получить доступ к элементам
списка, нам необходимо обращаться
по индексам. """
print("""Например 3-им элементом
списка выше будет:
""")
l = [6, 2, 5, 6, 2, 1, 9]
print(l[3])
##########################################
# TODO задание 1
##########################################
"""Выведите 5тый элемент списка"""
print("Результат задания 1")
l = [6, 2, 5, 6, 2, 1, 9]
print(l[5])     # здесь ваш код


##########################################
# конец задания
##########################################
"""
Так же с помощью обращения по индексу в списке
можно не только узнавать значение списка,
но и изменять его, например заменим 4ое значение"""
print("Старый l ", l)
l[4] = 356
print("Новый l", l)
"""
Теперь увеличим 5ое значение в 2 раза"""
print("Старый l", l)
l[5] = l[5] * 2
print("Новый l", l)
##########################################
# TODO задание 2
##########################################
"""Замените предпоследний элемент списка на 10"""
print("Результат задания 2")
l = [6, 2, 5, 6, 2, 1, 9]
l[-2] = 10      # здесь ваш код

print("Список после изменения", l)
##########################################
# конец задания
##########################################

##########################################
# TODO задание 3
##########################################
"""Уменьшите первый элемент в 3 раза"""
print("Результат задания 3")
l = [6, 2, 5, 6, 2, 1, 9]
l[1] = l[1] / 3        # здесь ваш код

print("Список после изменения", l)
##########################################
# конец задания
##########################################

"""
Индексы у списка l любой длинны изменяются от 0
до числа len(l) - 1
То есть выглядят так 0, 1, 2, 3, ..., len(l)
с помощью range, который мы рассматривали раньше
можно получить набор индексов любого списка
Пример:"""
print("""Индексами списка l = [9,3,6,2,4,6,2,4,5,3,2,4,6]
являются числа:
""")
l = [9, 3, 6, 2, 4, 6, 2, 4, 5, 3, 2, 4, 6]
for i in range(len(l)):
    print(i)
"""
в данном случае в range мы начинали с 0, закончили числом
len(l)(не включительно) - то есть как раз последним индексом
и шли с шагом 1"""
print("""
Раз мы можем с помощью такого фора получить 
доступ ко всем индексам, значит можем взаисодействовать
со всеми элементами списка. Например вывести их
(как ранее делали другим for)""")
l = [9, 3, 6, 2, 4, 6, 2, 4, 5, 3, 2, 4, 6]
for i in range(len(l)):
    print(l[i])

print("""
Или заменить все на 8
""")
l = [9, 3, 6, 2, 4, 6, 2, 4, 5, 3, 2, 4, 6]
print("Старый l", l)
for i in range(len(l)):
    l[i] = 8
print("Новый l", l)

print("""
Или все уменьшить в 4 раза
""")
l = [9, 3, 6, 2, 4, 6, 2, 4, 5, 3, 2, 4, 6]
print("Старый l", l)
for i in range(len(l)):
    l[i] = l[i] / 4
print("Новый l", l)

##########################################
# TODO задание 4
##########################################
"""Возвести каждый элемент во вторую степень"""
print("Результат задания 4")
l = [9, 3, 6, 2, 4, 6, 2, 4, 5, 3, 2, 4, 6]
for i in range(len(l)):     # здесь ваш for
    l[i] = l[i] ** 2

print("Список после изменения", l)
##########################################
# конец задания
##########################################

##########################################
# TODO задание 5
##########################################
"""Вычесть из каждого элемента результат 
выражения 32/5"""
print("Результат задания 5")
l = [9, 3, 6, 2, 4, 6, 2, 4, 5, 3, 2, 4, 6]
for i in range(len(l)):     # здесь ваш for
    l[i] = l[i] - 32 / 5
print("Список после изменения", l)
##########################################
# конец задания
##########################################


print("""
Так же как мы влияли на весь список,
так же можно повлиять и на часть, 
например увеличит вдвое все элементы, кроме
первого:
""")
l = [9, 3, 6, 2, 4, 6, 2, 4, 5, 3, 2, 4, 6]
print("Старый l", l)
for i in range(1, len(l)):
    l[i] = l[i] / 4
print("Новый l", l)
"""
Здесь важна 1 в range - которой раньше не было
"""

print("""
Или можем работать с элементами
с третьего по восьмой, например,
заменим их на 8ки
""")
l = [9, 3, 6, 2, 4, 6, 2, 4, 5, 3, 2, 4, 6]
print("Старый l", l)
for i in range(3, 8):
    l[i] = 8
print("Новый l", l)
"""
Стоит обратить внимание на изменения в range
"""


##########################################
# TODO задание 6
##########################################
"""Прибить к первым 5-ти элементам 16"""
print("Результат задания 6")
l = [9, 3, 6, 2, 4, 6, 2, 4, 5, 3, 2, 4, 6]
for i in range(0, 5):     # здесь ваш for
    l[i] = l[i] + 16
print("Список после изменения", l)

##########################################
# конец задания
##########################################

##########################################
# TODO задание 7
##########################################
"""Возвести в степень самого себя (a**a)
числа с индексами от 7 до 11"""
print("Результат задания 7")
l = [9, 3, 6, 2, 4, 6, 2, 4, 5, 3, 2, 4, 6]
for i in range(7, 12):      # здесь ваш for
    l[i] = l[i] ** l[i]
print("Список после изменения", l)

##########################################
# конец задания
##########################################