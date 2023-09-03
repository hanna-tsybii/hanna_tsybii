import sys
print(sys.argv)
def welcome_user(last_name, first_name, middle_name):
    # Виведення привітання
    print("Вітаю, {} {} {}!".format(last_name, first_name, middle_name))

if __name__ == "__main__":
    # Перевірка, чи передано необхідну кількість аргументів

    if len(sys.argv) != 4:
        print("Потрібно передати прізвище, ім'я та по-батькові як аргументи командного рядка.")
    else:
        last_name = sys.argv[1]
        first_name = sys.argv[2]
        middle_name = sys.argv[3]


        # Виклик функції привітання
        welcome_user(last_name, first_name, middle_name)
