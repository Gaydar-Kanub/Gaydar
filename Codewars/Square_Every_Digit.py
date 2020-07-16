def square_digits(num):
    res = ''
    for i in str(num):
        res += str(int(i) ** 2)
    return int(res)


if __name__ == "__main__":
    print(square_digits(9119))
