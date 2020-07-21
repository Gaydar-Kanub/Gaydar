def array_diff(a: list, b: list) -> list:
    return list(filter(lambda x: x not in b, a))