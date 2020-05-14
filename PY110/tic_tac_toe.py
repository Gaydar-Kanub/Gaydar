# Гайдаренко Евгений Григорьевич

ALL_WIN_COMBS = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]


def salute():
    print("\nПриветствую в игре 'крестики-нолики'.\n"
          "Введите количество игроков (1 или 2):")
    while True:
        x = input()
        try:
            x = int(x)
            if 1 <= x <= 2:
                break
            else:
                print("Количество игроков может быть только: 1 или 2. Попробуйте снова.")
        except ValueError:
            print('Некорректный ввод данных. Попробуйте снова.')
    return x


def game(x):
    play = True
    turn = False
    history = [' ' for _ in range(9)]
    b = False
    if x == 2:
        players = ['Игрок 1', 'Игрок 2']
    else:
        players = ['Игрок 1', 'компьютер']
    print(
        f'{players[0]} играет - Х, а {players[1]} играет - О')  # Сюда можно добавить выбор символа для каждого (посчитал это перегрузкой для терпения игрока - слишком много выбора плохо)
    while play:
        try:
            history.index(' ')
        except ValueError:
            return 'Ничья. Но вы не растраивайтесь - ИИ не удалось одержать вверх, а это уже победа!!!'
        turn = not (turn and True)
        if turn:
            sym = 'O'
            player = players[1]
        else:
            sym = 'X'
            player = players[0]
        z = 0
        if b:
            if player == 'компьютер':
                history = comp_go(history)
            else:
                history = go(history, player, sym)
            play = check_win(history, sym)
        else:
            b = True
        print('Игровое поле', '\t' * 2, 'Подсказка номеров поля')
        for i in range(5):
            line = ''
            if i % 2 == 1:
                line = '-' * 5 + '\t' * 5 + '-' * 5
            else:
                for _ in range(3):
                    line += history[z] + '|'
                    z += 1
                line = line[:-1] + '\t' * 5 + f'{z - 2}|{z - 1}|{z}'
            print(line)
        print('')
    return f'{player.capitalize()}, победил!!!'


def comp_go(history):
    win_combs = []
    lose_combs = []
    cell = 0
    for comb in ALL_WIN_COMBS:
        for i in comb:
            if history[i - 1] == 'X':
                lose_combs.append(comb)
                break
        else:
            win_combs.append(comb)
    for comb in lose_combs:
        n = 0
        for i in comb:
            if history[i - 1] == ' ':
                c = i
            elif history[i - 1] == 'X':
                n += 1
            else:
                break
        else:
            if n == 2:
                cell = c
                break
    else:
        for comb in win_combs:
            n = 0
            for i in comb:
                if history[i - 1] == 'O':
                    n += 1
                else:
                    c = i
            if n == 2:
                cell = c
                break
        else:
            for comb in lose_combs:
                for i in comb:
                    if history[i - 1] != ' ':
                        break
                    else:
                        c = i
                else:
                    cell = c
                    break
    if not cell:
        cell = history.index(' ') + 1
    print(f'Компьютер ставит O на {cell} клетку')
    history[cell - 1] = 'O'
    return history


def go(history, player, sym):
    while True:
        print(f'{player}, на какое поле вы хотите поставить {sym}?')
        x = input()
        try:
            x = int(x)
            if 1 > x or x > 9:
                print('Номер поля не может быть менее 1 и более 9. Попробуйте снова.')
            elif history[x - 1] != ' ':
                print('Это поле уже занято. Попробуйте другое.')
            else:
                break
        except ValueError:
            print('Некорректный ввод данных. Попробуйте снова.')
    history[x - 1] = sym
    return history


def check_win(history, sym):
    game_continue = True
    for comb in ALL_WIN_COMBS:
        for i in comb:
            if history[i - 1] != sym:
                break
        else:
            game_continue = False
    return game_continue


def tic_tac_toe():
    x = salute()
    res = game(x)
    return res


print(tic_tac_toe())
