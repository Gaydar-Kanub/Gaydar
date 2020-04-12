import numpy as np


def gen_new_field():
    sizeX, sizeY = 10, 10
    bomb_amount = 3
    # field = np.zeros((sizeX,sizeY))
    # for i in np.random.randint(0, sizeX*sizeY, bomb_amount):
    #     field[i // sizeX, i % sizeY] = -1
    # new_field = field.copy()
    # for x in range(field.shape[0]):
    #     for y in range(field.shape[1]):
    #         if field[x,y] != -1:
    #             new_field[x,y] = abs(field[x-1 if x-1 > 0 else 0: x+2 if x+2 < sizeX else sizeX,
    #                 y-1 if y-1 > 0 else 0: y+2 if y+2 < sizeY else sizeY].sum())
    visible_field = np.full((sizeX+1,sizeY+1),"▓")
    visible_field[:,0] = np.arange(0,sizeX + 1)
    visible_field[0,:] = np.arange(0,sizeY + 1)

    return visible_field#, new_field
print(gen_new_field())