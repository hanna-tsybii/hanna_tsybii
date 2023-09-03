def rotate_string(s, k):
    """
    Обертає рядок s на k символів вліво або вправо.

    Аргументи:
    s (str): Рядок, який потрібно обернути.
    k (int): Кількість символів, на які здійснюється обертання.
             Позитивне значення вказує на зсув вправо,
             від'ємне значення - на зсув вліво.

    Повертає:
    str: Обернутий рядок.
    """

    k = k % len(s)  # Нормалізуємо k до значення в межах довжини рядка s

    if k > 0:
        # Здійснюємо зсув вліво
        rotated = s[k:] + s[:k]
    else:
        # Здійснюємо зсув вправо
        rotated = s[k:] + s[:k]

    return rotated


if __name__ == '__main__':
    # Тест-кейси

    s1 = 'forwhomthebelltolls'
    k1 = 3
    expected1 = 'whomthebelltollsfor'
    result1 = rotate_string(s1, k1)
    print(f"Вхідний рядок: '{s1}', k = {k1}")
    print(f"Очікуваний результат: '{expected1}'")
    print(f"Отриманий результат: '{result1}'")
    print()

    s2 = 'verycomplexnumber'
    k2 = -6
    expected2 = 'numberverycomplex'
    result2 = rotate_string(s2, k2)
    print(f"Вхідний рядок: '{s2}', k = {k2}")
    print(f"Очікуваний результат: '{expected2}'")
    print(f"Отриманий результат: '{result2}'")
    print()
