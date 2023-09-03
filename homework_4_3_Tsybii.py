from decimal import Decimal

def calculate_taxes(income):
    income_decimal = Decimal(str(income))
    tax_rate = Decimal('0.18')  # 18% податок на доходи фізичних осіб
    military_tax_rate = Decimal('0.015')  # 1.5% військовий збір

    income_tax = income_decimal * tax_rate
    military_tax = income_decimal * military_tax_rate

    total_taxes = income_tax + military_tax

    return round(total_taxes, 2)

# Зчитування місячного доходу від користувача
income = input("Введіть місячний дохід: ")

# Обчислення суми податків
taxes = calculate_taxes(income)

# Виведення результату
print("Сума податків для сплати: ", taxes)
