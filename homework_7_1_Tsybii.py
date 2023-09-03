def find_last_person(n, k):
    # Створюємо список з числами від 1 до n
    circle = list(range(1, n + 1))
    index = 0 # Початковий індекс

    while len(circle) > 1:
        # Обчислюємо індекс людини, яку треба видалити
        index = (index + k - 1) % len(circle)
        # Видаляємо людину з кола
        circle.pop(index)

    return circle[0]

n = 10  # Кількість людей
k = 3   # Крок

last_person = find_last_person(n, k)
print("Номер останньої залишаючоїся людини:", last_person)
