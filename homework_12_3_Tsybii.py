def check_brackets(sequence):
    """
    Перевіряє, чи є послідовність дужок коректною.

    Аргументи:
    sequence (str): Послідовність дужок для перевірки.

    Повертає:
    bool: True, якщо послідовність дужок є коректною, False - в іншому випадку.
    """
    stack = []  # Стек для зберігання відкриваючих дужок

    opening_brackets = "([{<"
    closing_brackets = ")]}>"

    # Перебираємо кожен символ у послідовності
    for char in sequence:
        if char in opening_brackets:
            # Якщо символ є відкриваючою дужкою, додаємо його до стеку
            stack.append(char)
        elif char in closing_brackets:
            # Якщо символ є закриваючою дужкою
            if not stack:
                # Якщо стек пустий, це означає, що закриваюча дужка не має відповідної відкриваючої дужки
                return False

            # Отримуємо відповідну відкриваючу дужку
            opening_bracket = stack.pop()

            # Перевіряємо відповідність відкриваючої і закриваючої дужок
            if opening_brackets.index(opening_bracket) != closing_brackets.index(char):
                return False

    # Перевіряємо, чи всі відкриваючі дужки мають відповідні закриваючі дужки
    return len(stack) == 0


if __name__ == '__main__':
    # Тест-кейси

    test_cases = [
        "(((a * x) + [b] * y) + c",
        "auf(zlo)men [gy<psy>] four{s}"
    ]

    for sequence in test_cases:
        result = check_brackets(sequence)
        print(f"Послідовність '{sequence}': {result}")
