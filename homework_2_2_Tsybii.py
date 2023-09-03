import sys
print(sys.argv)

# Перевірка, чи передано необхідну кількість аргументів
if len(sys.argv) != 4:
    print("Потрібно передати арифметичну операцію та два числа як аргументи командного рядка.")
else:
    operation = sys.argv[1]
    num1 = float(sys.argv[2])
    num2 = float(sys.argv[3])

    # Виконання арифметичної операції
    result = None

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        result = num1 / num2

    # Виведення результату
    if result is not None:
        print(result)
