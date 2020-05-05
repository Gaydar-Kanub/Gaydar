def how_deep(structure):
    structure = str(structure)
    open = ['(', '[)]']
    close = [')', ']']
    count = max_deep = 0
    for i in structure:
        if i in open:
            count += 1
        elif i in close:
            count -= 1
        if count > max_deep:
            max_deep = count
    return max_deep


if __name__ == '__main__':
    print("Example:")
    print(how_deep((1, 2, 3)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert how_deep((1, 2, 3)) == 1
    assert how_deep((1, 2, (3,))) == 2
    assert how_deep((1, 2, (3, (4,)))) == 3
    assert how_deep(()) == 1
    assert how_deep(((),)) == 2
    assert how_deep((((),),)) == 3
    assert how_deep((1, (2,), (3,))) == 2
    assert how_deep((1, ((),), (3,))) == 3
    print("Coding complete? Click 'Check' to earn cool rewards!")
