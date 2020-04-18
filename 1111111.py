# import numpy as np
#
# a = np.arange(0,10)
# b = np.random.choice(a, 8)
# # a, b = gen_new_field()
# print(a)
# print(b)
# print(a[:3])

import numpy as np
np.random.seed(8)
def gen_new_field():
    sizeX, sizeY = 10, 10
    bomb_amount = 35
    field = np.zeros((sizeX,sizeY))
    for i in np.random.randint(0, sizeX*sizeY, bomb_amount):
        field[i // sizeX, i % sizeY] = -1
    new_field = field.copy()
    for x in range(field.shape[0]):
        for y in range(field.shape[1]):
            if field[x,y] != -1:
                new_field[x,y] = abs(field[x-1 if x-1 > 0 else 0: x+2 if x+2 < sizeX else sizeX,
                    y-1 if y-1 > 0 else 0: y+2 if y+2 < sizeY else sizeY].sum())
    visible_field = np.full((sizeX+1,sizeY+1),"▓")
    visible_field[:,0] = np.arange(-1,sizeX)
    visible_field[0,:] = np.arange(-1,sizeY)

    return new_field, visible_field


a, b = gen_new_field()
print(a)
print(b)