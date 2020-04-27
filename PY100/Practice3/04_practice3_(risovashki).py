# Представлено два рабочих варианта


# 1


def frame(width, height, depth=2, symbol='*'):
    if width < 2 * depth or height < 2 * depth or depth < 1:
        return 'Ошибка входных данных'
    print((symbol * width + '\n') * (depth - 1) + (symbol * width))
    wall = symbol * depth
    print((wall + ' ' * (width - 2 * depth) + wall + '\n') * (height - 2 * depth) + (wall + ' ' * (width - 2 * depth) + wall))
    return (symbol * width + '\n') * (depth - 1) + (symbol * width)


print(frame(8, 7, 1, '$'))


# 2


def frame(width, height, depth=2, symbol='*'):
    if width < 2 * depth or height < 2 * depth or depth < 1:
        return 'Рамка с такими параметрами физически невозможна. Упс!!!'
    print(up_down(width, depth, symbol))
    walls(width, height, depth, symbol)
    return up_down(width, depth, symbol)


def up_down(width, depth=2, symbol='*'):
    return (symbol * width + '\n') * (depth - 1) + (symbol * width)


def walls(width, height, depth, symbol):
    if height > (2 * depth):
        print(symbol * depth + ' ' * (width - 2 * depth) + symbol * depth)
        height -= 1
        return walls(width, height, depth, symbol)


print(frame(8, 8, 5, '$'))
