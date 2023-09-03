def convert_currency():
    units = ['', 'одна', 'дві', 'три', 'чотири', "п'ять", 'шість', 'сім', 'вісім', 'дев\'ять']
    tens = ['', '', 'двадцять', 'тридцять', 'сорок', 'п\'ятдесят', 'шістдесят', 'сімдесят', 'вісімдесят', 'дев\'яносто']
    teens = ['десять', 'одинадцять', 'дванадцять', 'тринадцять', 'чотирнадцять', 'п\'ятнадцять', 'шістнадцять', 'сімнадцять', 'вісімнадцять', 'дев\'ятнадцять']
    hundreds = ['', 'сто', 'двісті', 'триста', 'чотириста', 'п\'ятсот', 'шістсот', 'сімсот', 'вісімсот', 'дев\'ятсот']
    currency = ['гривень', 'гривня', 'гривні']
    coins = ['копійок', 'копійка', 'копійки']

    amount = float(input('Введіть суму: '))

    amount_str = "{:.2f}".format(amount)
    integer_part, decimal_part = amount_str.split('.')

    result = ''

    # Обробка цілої частини суми
    if integer_part == '0':
        result += 'нуль '
    else:
        integer_part = integer_part.zfill(6)
        millions = int(integer_part[0])
        thousands = int(integer_part[1:4])
        hundreds_part = int(integer_part[4:])

        if millions > 0:
            if millions == 1:
                result += 'один мільйон '
            elif millions < 5:
                result += units[millions] + ' мільйони '
            else:
                result += units[millions] + ' мільйонів '

        if thousands > 0:
            if thousands == 1:
                result += 'одна тисяча '
            elif thousands < 5:
                result += units[thousands] + ' тисячі '
            else:
                result += units[thousands] + ' тисяч '

        if hundreds_part > 0:
            if hundreds_part == 1:
                result += 'одна '
            elif hundreds_part < 5:
                result += units[hundreds_part] + ' '
            else:
                result += units[hundreds_part] + ' '

            if hundreds_part % 100 in range(10, 20):
                result += currency[2] + ' '
            elif hundreds_part % 10 == 1:
                result += currency[1] + ' '
            elif hundreds_part % 10 in range(2, 5):
                result += currency[0] + ' '
            else:
                result += currency[2] + ' '

    # Обробка десяткової частини суми
    decimal_part = int(decimal_part)
    if decimal_part > 0:
        result += str(decimal_part) + ' '

        if decimal_part % 100 in range(10, 20):
            result += coins[0] + ' '
        elif decimal_part % 10 == 1:
            result += coins[1] + ' '
        elif decimal_part % 10 in range(2, 5):
            result += coins[2] + ' '
        else:
            result += coins[0] + ' '

    print(result)


convert_currency()
