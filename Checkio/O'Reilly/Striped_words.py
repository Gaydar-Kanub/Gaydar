# def checkio(text):
#     VOWELS = "AEIOUY"
#     CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"
#     PUNCTUATIONS = "?.,:;|/{}[]()+-*=_ "
#     text = text.upper() + ' '
#     word = ''
#     wordss = []
#     words = []
#     number = 0
#     for i in text:
#         if i not in PUNCTUATIONS:
#             word += i
#         else:
#             wordss.append(word)
#             word = ''
#     for word in wordss:
#         if word.isalpha() and len(word) > 1:
#             words.append(word)
#     for word in words:
#         vo = co = False
#         if word[0] in VOWELS:
#             v, c = 0, 1
#         else:
#             v, c = 1, 0
#         for i in range(v, len(word), 2):
#             if word[i] not in VOWELS:
#                 vo = False
#                 break
#             else:
#                 vo = True
#         for j in range(c, len(word), 2):
#             if word[j] not in CONSONANTS:
#                 co = False
#                 break
#             else:
#                 co = True
#         if vo and co:
#             number +=1
#     return number


def checkio(text):
    VOWELS = "AEIOUY"
    CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"
    line = ''
    for sym in text:
        if sym.isalpha() or sym.isdigit():
            line += sym
        else:
            line += ' '
    line = line.upper()
    words = line.split(' ')
    count = 0
    for word in words:
        if word.isalpha() and len(word) > 1:
            for i in range(len(word) - 1):
                if word[i] in VOWELS and word[i + 1] in VOWELS or word[i] in CONSONANTS and word[i + 1] in CONSONANTS:
                    break
            else:
                count += 1
    return count


# print(checkio("My name is ..."))
# print(checkio("Hello world"))
# print(checkio("A quantity of striped words."))
# print(checkio("Dog,cat,mouse,bird.Human."))
print(checkio('To take a trivial example, which of us ever undertakes laborious physical exercise, except to obtain some advantage from it?'))
