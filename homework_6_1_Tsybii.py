def closest_mod_5(x):
    """
    Повертає найменше число y, яке задовольняє наступні умови:
    1. y >= x
    2. y % 5 == 0
    
    Аргументи:
    x (int): Вхідне ціле число.
    
    Повертає:
    int: Найменше число y, яке задовольняє вказані умови, або None, якщо такого числа немає.
    """
    if x % 5 == 0:
        return x
    return ((x // 5) + 1) * 5


cases = [
    # expected, input
    [5, 5],
    [15, 13],
    [0, 0],
    [0, -1],
    [-15, -16]
]

for i in cases:
    expected, inp = i
    res = closest_mod_5(inp)
    assert expected == res, 'Fail. Expected: {}\nActual: {}'.format(expected, res)
