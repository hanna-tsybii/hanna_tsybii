import random

def визначити_результат(гравець, компютер):
    if гравець == компютер:
        return "Нічия!"
    elif (гравець == "камінь" and компютер == "ножиці") or (гравець == "ножиці" and компютер == "папір") or (гравець == "папір" and компютер == "камінь"):
        return "Ви виграли!"
    else:
        return "Комп'ютер виграв!"

варіанти = ["камінь", "ножиці", "папір"]

while True:
    гравець = input("Введіть ваш вибір (камінь, ножиці, папір) або 'вийти' для завершення гри: ")
    гравець = гравець.lower()

    if гравець == "вийти":
        break

    if гравець not in варіанти:
        print("Невірний вибір. Спробуйте ще раз.")
        continue

    компютер = random.choice(варіанти)

    print(f"Ви обрали: {гравець}")
    print(f"Комп'ютер обрав: {компютер}")

    результат = визначити_результат(гравець, компютер)
    print(результат)
