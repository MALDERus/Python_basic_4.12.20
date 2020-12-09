while True:
    first_day_result = input("Введите результат пробежки за первый день\n>>>")
    if first_day_result.isdigit():
        first_day_result = int(first_day_result)
        break
    else:
        print("Вы ввели не число, пожалуйста введите число")

while True:
    needed_result = input("Введите цель пробежек в километрах\n>>>")
    if needed_result.isdigit():
        needed_result = int(needed_result)
        break
    else:
        print("Вы ввели не число, пожалуйста введите число")

day_count = 1

while first_day_result < needed_result:
    first_day_result *= 1.1
    day_count += 1

print(f"Вы достигните цели пробежек через {day_count} дней")
