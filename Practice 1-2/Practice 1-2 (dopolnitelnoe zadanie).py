def shokolad(n, m, k):
    step = 0
    if k < 1 or n < 1 or m < 1:
        return 'Ошибка ввода данных.'
    if n * m < k:
        return 'NO'
    elif n * m == k:
        pass
    elif k % n == 0 or k % m == 0:
        step = 1
    else:
        step += 2
        if n * m - max(n, m) > k > max(n, m) :
            step +=1
    return f'Получить шоколадку состоящую из долек колсчеством = {k} можно за количество разломов = {step}'


print(shokolad(13, 1, 13))