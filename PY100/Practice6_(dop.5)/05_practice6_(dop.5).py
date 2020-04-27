def blanket_001(W, H, hei):
    if hei < 3 or hei % 2 == 0:
        return 'Для красивого рисунка введите высоту ромба (hei) более 2 и не кратную 2.'
    for _ in range(H):
        for i in range(1, hei+1, 2):
            print(line_001(W, hei, i))
        for i in range(hei - 2, 0, -2):
            print(line_001(W, hei, i))
    return ''


def line_001(w, h, n):
    return (' ' * ((h - n) // 2) + '*' * n + ' ' * ((h - n) // 2) + ' ') * w


print(blanket_001(5, 3, 6))
