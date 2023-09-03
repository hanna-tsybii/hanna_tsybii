def binary(number):
    """
    Перетворює ціле число на його двійкове представлення.

    Аргументи:
    number (int): Вхідне ціле число.

    Повертає:
    str: Рядок, що представляє двійкове представлення числа.
    """
    if number == 0:
        return '0'

    result = ''
    while number > 0:
        remainder = number % 2
        result = str(remainder) + result
        number = number // 2

    return result


cases = [
    ['0', 0],
    ['1', 1],
    ['101', 5],
    ['110', 6],
    ['1011', 11],
    ['1100101', 101],
    ['100100101001', 2345],
]

for expected, number in cases:
    result = binary(number)
    assert expected == result, f"Wrong conversion.\nExpected: {expected}\nActual: {result}"
