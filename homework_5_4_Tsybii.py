import math

def solve_quadratic_equation(a, b, c):
    # Обчислення дискримінанту
    discriminant = b**2 - 4*a*c

    # Перевірка дискримінанту
    if discriminant > 0:
        # Два різних корені
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return x1, x2
    elif discriminant == 0:
        # Один подвійний корінь
        x = -b / (2*a)
        return x
    else:
        # Дискримінант менше нуля, корені відсутні
        return None

# Введення коефіцієнтів від користувача
a = float(input("Введіть коефіцієнт a: "))
b = float(input("Введіть коефіцієнт b: "))
c = float(input("Введіть коефіцієнт c: "))

# Вирішення квадратного рівняння
solution = solve_quadratic_equation(a, b, c)

# Виведення результату
if solution is None:
    print("Рівняння не має розв'язків")
elif isinstance(solution, tuple):
    x1, x2 = solution
    print("Рівняння має два корені: x1 =", x1, "x2 =", x2)
else:
    x = solution
    print("Рівняння має один корінь: x =", x)
