import numpy as np


np.random.seed(8)


def start_data():
    print('Приветствую вас в игре сапер!\n'
          'Через пробел введите размер поля и количество мин')
    x, y, mines = input().split(' ')
    x, y, mines = int(x), int(y), int(mines)
    while type(x) != type(y) != type(mines) != int:
        print('Некорректный ввод данных. Попробуйте снова')
        x, y, mines = input().split(' ')
        x, y, mines = int(x), int(y), int(mines)
    return x, y, mines


def gen_new_field(x, y, mines):
    true_field = np.full(x*y, 0)
    m = 0
    while mines > m:
        i = np.random.randint(0, x*y)
        if true_field[i] != -1:
            true_field[i] = -1
            m += 1
    true_field.shape = (x, y)
    visible_field = np.full((x+1, y+1), "▓")
    new_field = true_field.copy()
    for i in range(x):
        for j in range(y):
            if true_field[i, j] != -1:
                new_field[i, j] = abs(true_field[i-1 if i > 1 else 0: i+2,
                                                j-1 if j > 0 else 0: j+2]).sum()
    visible_field[:, 0] = np.arange(-1, x)
    visible_field[0, :] = np.arange(-1, y)
    return new_field, visible_field


def get_num():
    attempt = False
    while not attempt:
        print('Ваше предположение(x y):')
        try:
            i, j = input().split(' ')
            attempt = True
        except:
            print('Некорректно введеные данные.')
    return int(i), int(j)

def try_data(t_field, v_field, status):
    i, j = get_num()
    if t_field[i, j] == -1:
        v_field[i + 1, j + 1] = '*'
        # print('Упс!!! Вы подорвались!')
        status = 'lose'
    elif t_field[i, j] == 0:
        roster = find_empty(t_field, i, j)
        for z in roster:
            v_field[z[0]+1,z[1]+1] = t_field[z[0],z[1]]
    else:
        v_field[i+1, j+1] = str(t_field[i, j])
    print(v_field)
    return v_field, status


def find_empty(t_field, i, j):
    res = test_roster = [(i, j),]
    new = []
    while len(test_roster) != 0:
        for z in test_roster:
            if t_field[z[0], z[1]] == 0:
                for x in [z[0]-1, z[0], z[0]+1]:
                    if 0 <= x < len(t_field):
                        for y in [z[1]-1, z[1], z[1]+1]:
                            if 0 <= y < len(t_field[0]) and (x, y) not in res:
                                new.append((x, y))
        res += new
        test_roster, new = new, []
    return res

def game():
    x, y, mines = start_data()
    t_field, v_field = gen_new_field(x, y, mines)
    print(t_field)
    print(v_field)
    status = 'in game'
    while status == 'in game':
        v_field, status = try_data(t_field, v_field, status)
        if str(v_field).count("▓") == mines:
            status = 'win'
        if status == 'lose':
            return 'Упс!!! Вы подорвались!'
        elif status == 'win':
            return 'You are win!!!'

# a, b = gen_new_field(5, 5, 5)
# print(a)
# print(b)

print(game())
