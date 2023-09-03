import math

while True:
    a = float(input("Введіть число a (невід'ємне дійсне число): "))
    if a >= 0:
        break
    else:
        print("Число a повинно бути невід'ємним!")
        
while True:
    b = float(input("Введіть число b (невід'ємне дійсне число, відмінне від 0): "))
    if b >= 0 and b != 0:
        break
    else:
        print("Число b повинно бути невід'ємним і відмінним від 0!")

def calculate_result(a, b):
    x = (math.sqrt(a * b) / (b * (math.exp(a))) + a * math.exp(2 * a / b))
    return x

result = calculate_result(a, b)
print(result)
