# Сергей Дягилев
print("terminal_3")

import os
print("\033[1m" + "qwe", end = "\033[0;0m")
#проход по конкретному пути с выявлением файлов и папок
path
     = r"L:\Documents\Python\Look_in_structure\\"
print(os.listdir(path))
#print(os.path.isdir(r''))

#проход по всей структуре, не указывать глобальные папки, ограничиться конкретной местностью=)
for i in os.walk(path):
    print(i)

#os.mkdir(path + r'')# создание папки
#print(os.path.exist(path + r''))
#input()
#os.rmdir(path + r"n") #удаление папки
#print(os.path.exist(path + r''))

#os.startfile(r'')# запуск имеющегося файла
#for i in os.listdir(path):
#    if os.path.isdir(path)


