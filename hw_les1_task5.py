revenue = input("Введите значение выручки фирмы:\n>>>")

while not revenue.isdigit():
    revenue = input("Введите значение выручки фирмы:\n>>>")

costs = input("Введите значение издержек фирмы:\n>>>")

while not costs.isdigit():
    costs = input("Введите значение издержек фирмы:\n>>>")

if revenue.isdigit() and costs.isdigit():
    revenue = int(revenue)
    costs = int(costs)
else:
    print("Ошибка ввода значения, введите число.")
    exit()

if revenue > costs:
    revenue_profit = (revenue - costs) / revenue * 100
    print(f"Фирма сработала в прибыль. Рентабельность выручки составила: {revenue_profit}%")
else:
    print("Фирма сработала в убыток.")

eployee_count = input("Введите численность сотрудников в фирме:\n>>>")

if eployee_count.isdigit():
    eployee_count = int(eployee_count)
else:
    print("Ошибка ввода значения, введите число.")
    exit()

gain_per_employee = round((revenue - costs) / eployee_count, 2)

print(f"Прибыль фирмы в расчете на одного сотрудника составила: {gain_per_employee}")
