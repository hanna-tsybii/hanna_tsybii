def is_power_of_two(num):
    if num <= 0:
        return False
    return num & (num - 1) == 0

number = int(input("Введіть ціле додатнє число: "))

if number > 0:
    if is_power_of_two(number):
        print(f"{number} є степенем двійки.")
    else:
        print(f"{number} не є степенем двійки.")
else:
    print("Введене число має бути додатнім.")
