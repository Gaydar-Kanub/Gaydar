def remove_all_after(items: list, border: int):
    if len(items) != 0 and items.count(border) != 0:
        items = items[:items.index(border)+1]
    return items



if __name__ == '__main__':
    print("Example:")
    print(list(remove_all_after([1, 2, 3, 4, 5], 3)))
    print(list(remove_all_after([1, 1, 5, 6, 7], 2)))