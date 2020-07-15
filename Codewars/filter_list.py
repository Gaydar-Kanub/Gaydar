def filter_list(roster):
    return list(filter(lambda x: type(x) == int, roster))


if __name__ == "__main__":
    print(filter_list([1, 2, 'a', 'b']))
    print(filter_list([1, 'a', 'b', 0, 15]))
    print(filter_list([1, 2, 'aasf', '1', '123', 123]))