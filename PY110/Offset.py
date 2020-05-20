"""
Some text
"""

import random
import re
import json

LIBRARY = {'city': ['city1', 'city2', 'city3'],
           'street': ['street1', 'street2', 'street3']}


def mk_dec_check_test(line):
    """This decorator fabric get 'line' for function 'iner'"""

    def check_address(func):
        """This decorator check any argument == 'line'"""

        def inner(*args):
            if any(x == line for x in args):
                return f'Вызов функции {func.__name__} с параметрами {args}'
            else:
                gen = func(*args)
                res = next(gen)
                if all(check_spelling(x) for x in json.loads(res)):
                    return res
                else:
                    raise ValueError

        return inner

    return check_address


@mk_dec_check_test('test')
def get_address():
    """This function - generator return generated address"""
    while True:
        city = random.choice(LIBRARY['city'])
        street = random.choice(LIBRARY['street'])
        house = random.randint(1, 100)
        room = random.randint(1, 150)
        res = {'city': city, 'street': street, 'house': str(house), 'room': str(room)}
        if random.randint(0, 1) == 1:
            res['build'] = random.randint(1, 5)
        res = json.dumps(res)
        with open('adr.txt', 'w') as file:
            file.write(res)
        yield res


def check_spelling(x):
    """This function check 'x' consist of letters and/or numbers"""
    if re.fullmatch(r'\w+', x):
        res = True
    else:
        res = False
    return res


print(get_address())
