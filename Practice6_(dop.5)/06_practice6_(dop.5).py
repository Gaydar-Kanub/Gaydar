import numpy as np
np.random.seed(8)


def new_field(sizeX, sizeY, bombs):
    admin_field = np.zeros((sizeX, sizeY))
    arr = np.arange(0, (sizeX-1) * (sizeY-1))
    np.random.shuffle(arr)
    for i in arr[:bombs]:
        admin_field[i//(sizeX-1) + 1, i%(sizeX-1) + 1] = -1
    print(admin_field)
    for x in range(admin_field.shape[0]):
        for y in range(admin_field.shape[1]):
            if admin_field[x, y] != -1:
                admin_field[x,y] = abs(admin_field[x-1 if x-1 > 0 else 0: x+2 if x+2 < sizeX else sizeX,
                                       y-1 if y-1 > 0 else 0: y+2 if y+2 < sizeY else sizeY].sum())

    user_field = np.full((sizeX + 1, sizeY + 1), '▓')
    user_field[:, 0] = np.arange(-1, sizeX)
    user_field[0, :] = np.arange(-1, sizeY)

    return admin_field, user_field


admin_field, user_field = new_field(5, 5, 7)

print(admin_field)
print(user_field)
