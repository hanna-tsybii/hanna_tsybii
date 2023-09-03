def calculate_mean(arr):
    if len(arr) == 0:
        return None
    return sum(arr) / len(arr)

def calculate_median(arr):
    sorted_arr = sorted(arr)
    n = len(sorted_arr)
    if n % 2 == 0:
        # Якщо кількість елементів парна, обчислюємо середнє двох центральних елементів
        mid = n // 2
        return (sorted_arr[mid - 1] + sorted_arr[mid]) / 2
    else:
        # Якщо кількість елементів непарна, повертаємо значення середнього елемента
        mid = n // 2
        return sorted_arr[mid]

# Приклад використання
numbers = [7, 45, 7, 19, 4, 1]
mean = calculate_mean(numbers)
median = calculate_median(numbers)
print("Середнє значення:", mean)
print("Медіана:", median)
