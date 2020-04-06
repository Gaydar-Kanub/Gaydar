def goes_after(word: str, first: str, second: str):
    if first != second and first in word and second in word:
        if word[word.index(first)+1] == second and word.index(first) < word.index(second):
            return True
    return False


if __name__ == '__main__':
    print("Example:")
    print(goes_after('world', 'w', 'o'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert goes_after('world', 'w', 'o') == True
    assert goes_after('world', 'l', 'o') == False
    assert goes_after('panorama', 'a', 'n') == True
    assert goes_after('list', 'l', 'o') == False
    assert goes_after('', 'l', 'o') == False
    assert goes_after('list', 'l', 'l') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")