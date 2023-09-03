def random_number_generator(seed):
    current_number = seed

    while True:
        x1, x2 = current_number // 1000, current_number % 1000
        y = x2 * 1000 + x1
        multiplied = x1 * y
        result = (multiplied // 1000) % 1000000
        yield result
        current_number = result

if __name__ == "__main__":
    seed = 654321
    generator = random_number_generator(seed)

    for _ in range(16):  # Виправляємо кількість генерованих чисел, щоб збігалася з тест-кейсом.
        random_num = next(generator)
        print(random_num)
