# # Задача №1 - Определение вариантов оплаты
#
# def buy(rating_A, amount_A, rating_B, amount_B, price):
#     result = 'Возможные варианты расплатиться без сдачи:\n'
#     if rating_A * amount_A + rating_B * amount_B < price:
#         return 'Недостаточно денег'
#     if rating_A > price and rating_B > price:
#         return 'Без сдачи никак не расплатиться'
#     elif rating_A < price and rating_B > price:
#         if price % rating_A == 0 and price / rating_A < amount_A:
#             return result + coin_calc(amount_A, rating_A, price)
#     elif rating_A > price and rating_B < price:
#         if price % rating_B == 0 and price / rating_B < amount_A:
#             return result + coin_calc(amount_B, rating_B, price)
#     else:
#         for i in range(min(price // rating_A, amount_A) + 1):
#             summ_A = i * rating_A
#             rest = price - summ_A
#             if (rest) % rating_B == 0 and (rest) / rating_B <= amount_B:
#                 result +=  f'{i} {coin(i)} номиналом {rating_A} и ' + coin_calc(amount_B, rating_B, rest) + '\n'
#         return result
#
#
# def coin_calc(amount, rating, price):
#     if price % rating == 0 and price / rating <= amount:
#         amo = int(price / rating)
#         return f'{amo} {coin(amo)} номиналом {rating}'
#
#
# def coin(amount):
#     if amount % 10 == 1:
#         coin = 'монетой'
#     else:
#         coin = 'монетами'
#     return coin
#
#
# print(buy(5, 10, 10, 6, 100))
#
#
# # Задача 2 - Определение количесива разрядов в числе
# print('Введите число, у которого необходимо посчитать кол-во разрядов')
# num = input()
# print(len(num))


# Задача 3 - Определение палиндрома
# print('Введите строку, которую необходимо проверить на полиндром')
# line = input()
# line.lower()
# line2 = ''
# palindrom = 'Эта строка является палиндромом'
# for symbol in line:
#     if '0' <= symbol <= '9' or 'a' <= symbol <= 'z':
#         line2 += symbol
# for i in range(len(line2) // 2):
#     if line2[i] != line2[-i - 1]:
#         palindrom = 'Эта строка не палиндром'
# print(palindrom)
