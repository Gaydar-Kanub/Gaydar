import numpy as np

np.random.seed(8)


def gen_new_field():
    sizeX, sizeY = 10, 10
    bomb_amount = 3
    field = np.zeros((sizeX, sizeY))
    for i in np.random.randint(0, sizeX * sizeY, bomb_amount):
        field[i // sizeX, i % sizeY] = -1
    new_field = field.copy()
    for x in range(field.shape[0]):
        for y in range(field.shape[1]):
            if field[x, y] != -1:
                new_field[x, y] = abs(field[x - 1 if x - 1 > 0 else 0: x + 2 if x + 2 < sizeX else sizeX,
                                      y - 1 if y - 1 > 0 else 0: y + 2 if y + 2 < sizeY else sizeY].sum())
    visible_field = np.full((sizeX + 1, sizeY + 1), "▓")
    visible_field[:, 0] = np.arange(-1, sizeX)
    visible_field[0, :] = np.arange(-1, sizeY)

    return new_field, visible_field


def get_nums():
    x, y = input("введите:\n").split(" ")
    x, y = int(x), int(y)
    return x, y


def find_empty(x, y, field):
    to_visit = [(x, y)]
    for i in to_visit:
        if x - 1 > 0 and field[x - 1, y] == 0 and (x - 1, y) not in to_visit:
            to_visit.append((x - 1, y))
        if y - 1 > 0 and field[x, y - 1] == 0 and (x, y - 1) not in to_visit:
            to_visit.append((x, y - 1))
        if x + 1 < field.shape[0] and field[x + 1, y] == 0 and (x + 1, y) not in to_visit:
            to_visit.append((x + 1, y))
        if y + 1 < field.shape[1] and field[x, y + 1] == 0 and (x, y + 1) not in to_visit:
            to_visit.append((x, y + 1))
    return to_visit


field, visible = gen_new_field()
print(field)
status = "game"
while status == "game":
    print(visible)
    x, y = get_nums()
    if field[x, y] == -1:
        print("Вы проиграли")
        visible[x + 1, y + 1] = "*"
        status = "lose"
    elif field[x, y] in (1, 2, 3, 4, 5, 6, 7, 8):
        visible[x + 1, y + 1] = str(field[x, y])
    else:
        tv = find_empty(x, y, field)
        print(tv)
        for i in tv:
            visible[i[0] + 1, i[1] + 1] = " "
    if status != "lose" and ((visible == "▓").sum() == (field == -1).sum()):
        print("Вы выиграли")
        status = "win"
