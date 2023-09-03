def is_palindrome(phrase):
    """
    Перевіряє, чи є фраза паліндромом.

    Аргументи:
    phrase (str): Фраза, яку потрібно перевірити.

    Повертає:
    bool: True, якщо фраза є паліндромом, False - в іншому випадку.
    """
    # Перетворення фрази на нижній регістр і видалення пробілів
    phrase = phrase.lower().replace(" ", "")

    # Порівняння фрази з її реверсним варіантом
    if phrase == phrase[::-1]:
        return True
    else:
        return False


if __name__ == '__main__':
    # Точка входу

    phrases = [
        "Was it a cat I saw",
        "No x in Nixon",
        "А роза упала на лапу Азора",
        "Три психи пили Пилипихи спирт",
        "Вор Азаров"
    ]

    for phrase in phrases:
        result = is_palindrome(phrase)
        print(f"Фраза '{phrase}': {result}")
