def read_log_file(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line

def calculate_bytes_sum(log_file):
    sent_bytes = 0
    received_bytes = 0
    for log_entry in log_file:
        fields = log_entry.split(' ')
        if len(fields) >= 11:
            # Перевірка, чи у лог-записі є щонайменше 11 полів, що містить дані про байти.
            try:
                sent_bytes += int(fields[9])
                # Знаходження надісланих байтів та додавання їх до загальної суми.
                received_bytes += int(fields[10])
                # Знаходження прийнятих байтів та додавання їх до загальної суми.
            except ValueError:
                # Якщо поле не може бути перетворено в ціле число (наприклад, містить некоректні дані),
                # то ігноруємо цей запис логу та переходимо до наступного.
                continue

    return sent_bytes, received_bytes

if __name__ == "__main__":
    log_file = read_log_file("2017_05_07_nginx.txt")
    # Відкриваємо файл для обробки
    total_sent_bytes, total_received_bytes = calculate_bytes_sum(log_file)
    # Обчислюємо сумарні байти

    # Виводимо результати
    print("Сумарна кількість надісланих байтів:", total_sent_bytes)
    print("Сумарна кількість прийнятих байтів:", total_received_bytes)
