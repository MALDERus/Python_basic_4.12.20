def division_numbers(a, b):
    """
    Делит число а на число b, выводит ошибку при делении на 0
    :param a: делимое
    :param b: делитель
    :return: результат деления, округление до 2 знаков
    """
    try:
        return (round((a / b), 2))
    except ZeroDivisionError:
        print("Деление на НОЛЬ!")

result = division_numbers(a=int(input("Введите делимое число\n>>>")), b=int(input("Введите делитель\n>>>")))

print(result)
