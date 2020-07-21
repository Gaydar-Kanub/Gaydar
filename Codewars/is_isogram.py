def is_isogram(string: str) -> bool:
    return len(string) == len(set(string.lower()))
