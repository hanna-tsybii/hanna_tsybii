def calculate_period(amount, expected, percent):
    """
    Повертає кількість років необхідних для зростання депозиту до потрібної суми.

    Аргументи:
    amount (float): Наявна сума грошей на депозиті.
    expected (float): Потрібна сума грошей.
    percent (float): Річний банківський процент по депозиту.

    Повертає:
    int: Кількість років необхідних для зростання депозиту до потрібної суми.
         Якщо потрібна сума недосяжна або вхідні дані некоректні, повертає None.
    """
    if amount < 0 or expected < 0 or percent <= 0:
        return None

    years = 0
    while amount < expected:
        amount += amount * (percent / 100)
        years += 1

    return years


cases = [
    [30, (1000, 10000, 8)],
    [22, (40000, 1000000, 16)],
    [None, (1000, -20000, 8)]
]

for expected, inputs in cases:
    result = calculate_period(*inputs)
    assert expected == result, f"Wrong conversion.\nExpected: {expected}\nActual: {result}"
