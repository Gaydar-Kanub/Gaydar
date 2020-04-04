def buy_001(rating_a, amount_a, rating_b, amount_b, price):
    result = 'Возможные варианты расплатиться без сдачи:\n'
    if rating_a * amount_a + rating_b * amount_b < price:
        return 'Недостаточно денег'
    if rating_a > price and rating_b > price:
        return 'Без сдачи никак не расплатиться'
    elif rating_a < price < rating_b:
        if price % rating_a == 0 and price / rating_a < amount_a:
            return result + coin_calc_001(amount_a, rating_a, price)
    elif rating_a > price > rating_b:
        if price % rating_b == 0 and price / rating_b < amount_a:
            return result + coin_calc_001(amount_b, rating_b, price)
    else:
        for i in range(min(price // rating_a, amount_a) + 1):
            summ_a = i * rating_a
            rest = price - summ_a
            if rest % rating_b == 0 and rest / rating_b <= amount_b:
                result += f'{i} {coin_001(i)} номиналом {rating_a} и ' + coin_calc_001(amount_b, rating_b, rest) + '\n'
        return result


def coin_calc_001(amount, rating, price):
    if price % rating == 0 and price / rating <= amount:
        amo = int(price / rating)
        return f'{amo} {coin_001(amo)} номиналом {rating}'


def coin_001(amount):
    if amount % 10 == 1:
        coin = 'монетой'
    else:
        coin = 'монетами'
    return coin


# print(buy_001(20, 10, 10, 6, 100))


def determ_002():
    num = ''
    while not num.isdigit():
        print('Введите число в цифровомформате, у которого необходимо посчитать кол-во разрядов')
        num = input()
    return f'Количество разрядов = {len(num)}'

# print(determ_002())


def palindrom_003():
    print('Введите строку, которую необходимо проверить на полиндром')
    line = input()
    line.lower()
    line2 = ''
    result = 'Эта строка является палиндромом'
    for symbol in line:
        if '0' <= symbol <= '9' or 'a' <= symbol <= 'z':
            line2 += symbol
    for i in range(len(line2) // 2):
        if line2[i] != line2[-i - 1]:
            result = 'Эта строка не палиндром'
    return result


# print(palindrom_003())


def rep_004(line, subline1='111', subline2='example'):
    return line.replace(subline1, subline2, -1)


# print(rep_004('fgdfg111fd 11 1 d1111 dfgdfg11 121'))
