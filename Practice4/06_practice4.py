def initial_data_001():
    state = False
    while not state:
        print(f'\nЧерез запятую ведите число для перевода, исходную сист.счисления, конечную сист.счисления:')
        data = input()
        if data == 'STOP':
            return 'Жаль что не получилось вместе поработать!'
        data = data.replace(' ', '').split(',')
        if len(data) != 3:
            print('''Недостаточно исзодных данных. Попробуйте снова. Если же вы хотите прекратить, то введите: STOP''')
            continue
        for i in range(1, 3):
            if not data[i].isdigit():
                print('Системы счисления необходимо указывать в цифровом виде. Попробуйте снова.\n'
                      'Если же вы хотите прекратить, то введите: STOP')
                break
        else:
            for i in data[0]:
                if int(data[1]) <= 10:
                    if not i.isdigit() or int(i) >= int(data[1]):
                        print('Недопустимые символы для данной системы счисления. Попробуйте снова.\n'
                              'Если же вы хотите прекратить, то введите: STOP')
                        break
                else:
                    if i > chr(int(data[1]) - 10 + 96):  # chr(97) == 'a' - оставил в таком виде для удобства чтения
                        print('Недопустимые символы для данной системы счисления. Попробуйте снова.\n'
                              'Если же вы хотите прекратить, то введите: STOP')
                        break
            else:
                state = True
    return data


def num_sys_initial_10_001(num, num_sys):
    dec = 0
    for i in range(len(num)):
        sym = num[-i - 1]
        if 'a' <= sym <= 'z':
            sym = ord('a') - ord(sym) + 10
        dec += int(sym) * int(num_sys) ** i
    return dec


# print(num_sys_initial_10_001())


def num_sys_10_final_001(dec, num_sys):
    num = ''
    if dec == 0:
        return '0'
    while dec > 0:
        rest = dec % int(num_sys)
        if rest > 9:
            num += chr(97 + rest - 10)  # chr(97) == 'a' - оставил в таком виде для удобства чтения
        else:
            num += str(rest)
        dec = dec // int(num_sys)
    return num[::-1]


# print(num_sys_10_16_004())


def num_sys_initial_final_001():
    data = initial_data_001()
    dec = num_sys_initial_10_001(data[0], data[1])
    final = num_sys_10_final_001(dec, data[2])
    return final


# print(num_sys_initial_final_001())


def change_num_syst_002():
    print('\nДобро пожаловать в программу перевода чисел из одной системы счисления в другую!')
    answer = 'Y'
    while answer == 'Y':
        print(num_sys_initial_final_001())
        print('Если желаете продолжить, введите: Y')
        answer = input()
    return 'Спасибо что воспользовались программой!'


print(change_num_syst_002())