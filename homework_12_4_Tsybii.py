def encrypt_message(message):
    """
    Здійснює елементарне шифрування повідомлення шляхом заміни кожної літери сусідньою справа за абеткою.

    Аргументи:
    message (str): Повідомлення для шифрування.

    Повертає:
    str: Зашифроване повідомлення.
    """
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            # Знаходимо наступну літеру у алфавіті
            next_char = chr((ord(char) - ord('a') + 1) % 26 + ord('a'))
            encrypted_message += next_char
        else:
            # Залишаємо символи, які не є літерами без змін
            encrypted_message += char
    return encrypted_message


if __name__ == '__main__':
    # Точка входу

    message = "vasia"
    encrypted_message = encrypt_message(message)
    print(f"Повідомлення: {message}")
    print(f"Зашифроване повідомлення: {encrypted_message}")
