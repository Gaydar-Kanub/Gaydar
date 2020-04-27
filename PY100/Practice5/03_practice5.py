import os

# way = r'C:\Users\Evgen\Desktop\Python\Practice5'
way = os.getcwd()       # Вместо заданной папки


def mkdirectories():
    os.makedirs(way + "\\dir1\\dir2")
    os.makedirs(way + "\\dir1\\dir3\\dir4")
    file = open(way + "\\dir1\\dir3\\dir4\\" + 'file4.txt', 'w')
    file.close()
    os.makedirs(way + "\\dir1\\dir4")
    os.makedirs(way + '\\dir2\\dir3\\dir4')
    file = open(way + "\\dir2\\dir3\\dir4\\" + 'file4.txt', 'w')
    file.close()
    os.makedirs(way + '\\dir2\\dir4')
    file = open(way + "\\dir2\\dir4\\" + 'file4.txt', 'w')
    file.close()


mkdirectories()
