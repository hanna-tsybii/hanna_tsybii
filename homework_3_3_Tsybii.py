height = float(input("Введіть ваш зріст в метрах: "))
weight = float(input("Введіть вашу вагу в кілограмах: "))

bmi = weight / (height ** 2)

print("Ваш індекс маси тіла (BMI):", bmi)

if bmi < 18.5:
    print("Недостатня вага")
elif bmi >= 18.5 and bmi <= 24.9:
    print("Нормальна вага")
elif bmi >= 25 and bmi <= 29.9:
    print("Надмірна вага")
else:
    print("Ожиріння")
input()
