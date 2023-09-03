def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Зчитуємо температуру за Фаренгейтом від користувача
fahrenheit = float(input("Введіть температуру за Фаренгейтом: "))

# Викликаємо функцію для перетворення значення
celsius = fahrenheit_to_celsius(fahrenheit)

# Виводимо перетворене значення за Цельсієм
print("Температура за Цельсієм:", celsius)

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Зчитуємо температуру за Цельсієм від користувача
celsius = float(input("Введіть температуру за Цельсієм: "))

# Викликаємо функцію для перетворення значення
fahrenheit = celsius_to_fahrenheit(celsius)

# Виводимо перетворене значення за Фаренгейтом
print("Температура за Фаренгейтом:", fahrenheit)
