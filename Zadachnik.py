# Перевод Цельсий в Фаренгейт
def cel_far_003():
    cel = ''
    while not cel.isdigit():
        print('Ведите температуру в Цельсиях для перевода в Фаренгейты.'
              'Ели хотите прекратить выполнение задачи наберите: S')
        cel = input()
        if cel == 'S':
            return 'Вы прервали выполнение программы.'
    far = int(cel) * 0.8 + 32
    return far


print(cel_far_003())


# Проверка правильности ввода номера кредитки
def alg_luhn_004(num):
    num = num.replace(' ', '')
    if len(num) % 2 == 0:
        start = 1
    else:
        start = 0
    for i in range(start, len(num), 2):
        if int(num[i]) * 2 > 9:
            num = num[:i] + str(int(num[i]) * 2 - 9) + num[i+1:]
    s = sum(map(int, list(num)))
    if s % 10 == 0:
        result = 'Проверка пройдена!'
    else:
        result = 'Увы!!!'
    return result


nums = ['4561 2612 1234 5467', '4561 2612 1234 5464']
print(alg_luhn_004(nums[1]))
