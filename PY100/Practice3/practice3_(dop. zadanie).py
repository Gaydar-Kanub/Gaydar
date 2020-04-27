def game():
    print('Приветствую в игре "Быки и коровы"')
    number = num()
    result = False
    n = 0
    while not result:
        attempt = att()
        n += 1
        result = guess(number, attempt)
        if bulls(number, attempt) == 4:
            return f'Поздравляю с победой!!! \nВы справились за {n} попыток.'
        amount_bull = bulls(number, attempt)
        amount_cow = cows(number, attempt, amount_bull)
        print(f"{amount_cow} {word_cow_bull(amount_cow, 'cow')} и {amount_bull} {word_cow_bull(amount_bull, 'bull')}")


def num():
    import random
    ran = str(random.random())
    number = ''
    for i in ran[2:]:
        if i not in number:
            number += i
            if len(number) == 4:
                return number


def att():
    print('Попробуй угадать 4-х значное число')
    line = input()
    while len(line) != 4 or not line.isdigit():
        print('Необходимо ввести число, состоящее из четырех цифр')
        line = input()
    return line


def guess(number, attempt):
    if number == attempt:
        return True
    else:
        return False


def bulls(number, attempt):
    bull = 0
    for i in range(len(number)):
        if number[i] == attempt[i]:
            bull += 1
    return bull


def cows(number, attempt, amount_bull):
    cow = 0
    for i in number:
        if i in attempt:
            cow += 1
    return cow - amount_bull


def word_cow_bull(amount, c_b):
    if c_b == 'cow':
        words = ['коров', 'корова', 'коровы']
    elif c_b == 'bull':
        words = ['быков', 'бык', 'быка']
    if amount == 0:
        word = words[0]
    elif amount == 1:
        word = words[1]
    else:
        word = words[2]
    return word


print(game())
