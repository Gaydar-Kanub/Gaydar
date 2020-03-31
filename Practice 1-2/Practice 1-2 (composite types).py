full_name = 'Гайдаренко Евгений'
N = (len(full_name.split(' ')[0]) - len(full_name.split(' ')[1])) % 5
print(N)

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Тип данных - List
print('List')
roster = [i for i in range((N + 2) * 2)]                                # п.1
roster += [i + 1 for i in roster]                                       # п.2
choice_roster3 = roster[roster.index(sorted(roster)[-2]): -1]           # п.3
choice_roster4 = [roster[i] for i in range(len(roster)) if i % 3 == 1]  # п.4 - Либо см.ниже закомент.строку
# choice_roster4 = roster[1::3]                                         # п.4


def choice_roster5(roster, num_third=1):                                # п.5
    third = round(len(roster) / 3)                                      # п.5
    if num_third == 3:                                                  # п.5
        return roster[-third:]                                          # п.5
    return roster[(num_third - 1) * third: num_third * third]           # п.5


print(roster)
print(choice_roster5(roster, 3))


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Тип данных - Tuple
print('Tuple')
cortege = tuple()                           # п.1
for i in range((N + 2) * 2):                # п.1
    cortege += (i,)                         # п.1
for i in cortege:                           # п.2
    cortege += (i + 1,)                     # п.2
choice_cortege3 = cortege[cortege.index(sorted(cortege)[-2]): -1]    # п.3
choice_cortege4 = tuple()                   # п.4 - Либо одной строчкой (см.ниже закомент.строку)
for i in range(len(cortege)):               # п.4 - Либо одной строчкой (см.ниже закомент.строку)
    if i % 3 == 1:                          # п.4 - Либо одной строчкой (см.ниже закомент.строку)
        choice_cortege4 += (cortege[i], )   # п.4 - Либо одной строчкой (см.ниже закомент.строку)
# choice_cortege4 = cortege[1::3]           # п.4


def choice_cortege5(cortege, num_third=1):                              # п.5
    third = round(len(cortege) / 3)                                     # п.5
    if num_third == 3:                                                  # п.5
        return cortege[-third:]                                         # п.5
    return cortege[(num_third - 1) * third: num_third * third]          # п.5


print(cortege)
print(choice_cortege5(cortege))


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Тип данных - Set
print('Set')
many = {i for i in range((N + 2) * 2)}      # п.1
many = many.union({i + 1 for i in many})    # п.2
print(many)
# п.3 Не возможно выполнить, т.к. мномество является неупорядоченным набором эелементов.
# п.4 Не возможно выполнить, т.к. мномество является неупорядоченным набором эелементов (нет индексов).
choice_many5 = {many.pop() for _ in range(round(len(many) / 3))}    # п.5 - невозможно задать номер трети, т.к. это множество


print(choice_many5)


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Тип данных - Dictionary
print('Dictionary')
vocabulary = {i: i for i in range((N + 2) * 2)}                                         # п.1
vocabulary.update({i[0] + 1: i[1] + 1 for i in vocabulary.items()})                     # п.2
print(vocabulary)
# п.3 Не возможно выполнить, т.к. словарь является неупорядоченным коллекцией.
choice_vocabulary4 = {i: vocabulary[i] for i in vocabulary if vocabulary[i] % 3 == 1}   # п.4
choice_vocabulary5 = {vocabulary.popitem() for i in range(round(len(vocabulary) / 3))}  # п.5


print(choice_vocabulary5)


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Тип данных - String
print('String')
line = ''                                   # п.1
for i in range((N + 2) * 2):                # п.1
    line += str(i)                          # п.1
for i in line:                              # п.2
    line += str(int(i) + 1)                 # п.2
choice_line3 = line[line.index(sorted(line)[-2]): -1]    # п.3
choice_line4 = ''                           # п.4 - Либо одной строчкой (см.ниже закомент.строку)
for i in range(len(line)):                  # п.4 - Либо одной строчкой (см.ниже закомент.строку)
    if i % 3 == 1:                          # п.4 - Либо одной строчкой (см.ниже закомент.строку)
        choice_line4 += line[i]             # п.4 - Либо одной строчкой (см.ниже закомент.строку)
# choice_line4 = line[1::3]                 # п.4


def choice_line5(line, num_third=1):                            # п.5
    third = round(len(line) / 3)                                # п.5
    if num_third == 3:                                          # п.5
        return line[-third:]                                    # п.5
    return line[(num_third - 1) * third: num_third * third]     # п.5


print(line)
print(choice_line5(line, 3))
