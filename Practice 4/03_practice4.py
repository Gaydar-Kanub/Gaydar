import random


def guess_game_001_lev1(num=random.randint(1, 100)):
    print('\nДобро пожаловать в игру по угадыванию чисел!!!\n')
    result = ''
    while result != 'Да, это оно!!!':
        guess = guess_001_lev1()
        if int(guess) < num:
            result = 'Загаданное число больше\n'
        elif int(guess) > num:
            result = 'Загаданное число меньше\n'
        else:
            return 'Да, это оно!!!'
        print(result)


def guess_001_lev1():
    print('Введите своё предположение')
    guess = input()
    while not guess.isdigit():
        print('Неккоректный ввод данных. Попробуйте снова')
        guess = input()
    return guess


# print(guess_game_001_lev1())


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


def guess_game_001_lev2():
    repeat = 'да'
    games = 0
    while repeat == 'да':
        print(guess_game_001_lev1(random.randint(1, 100)))
        print('\nЕсли хотите ли сыграть ещё, то введите: да')
        repeat = input()
        games += 1
    return f'Количество проведенных партий = {games}'


# print(guess_game_001_lev2())


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


def guess_game_001_lev3(num=random.randint(1, 100)):
    print('\nДобро пожаловать в игру по угадыванию чисел!!!\n')
    moves = 0
    games = 0
    while moves < 50:
        print(f'Количество оставшихся ходов: {50 - moves}')
        result = ''
        while result != 'Да, это оно!!!':
            guess = guess_001_lev3()
            moves += 1
            if moves > 50:
                return 'Вы исчерпали лимит ходов'
            if int(guess) < num:
                result = 'Загаданное число больше\n'
            elif int(guess) > num:
                result = 'Загаданное число меньше\n'
            else:
                games += 1
                result = 'Да, это оно!!!'
            print(result)
        print('Давайте сыграем ещё раз')
        num = random.randint(1, 10)
    return f'Количество выигранных партий: {games}'


def guess_001_lev3():
    print('Введите своё предположение')
    guess = input()
    while not guess.isdigit():
        print('Неккоректный ввод данных. Попробуйте снова')
        guess = input()
    return guess


print(guess_game_001_lev3())
