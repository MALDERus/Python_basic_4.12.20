def mult():
    user_str = input("Введите строку чисел, разделенных пробелом\n>>>").split()
    result = 0
    for el in user_str:
        result = result + int(el)
    return result

total_sum = 0

while True:
    try:
        total_sum = total_sum + mult()
    except ValueError as e:
        user_str = input("Пожалуйста,ещё раз введите эту строку чисел, разделенных пробелом\n>>>").split()
        result1 = 0
        for i in user_str:
            if i.isdigit():
                result1 += int(i)
            else:
                break
        total_sum = total_sum + result1
        break

print(total_sum)
