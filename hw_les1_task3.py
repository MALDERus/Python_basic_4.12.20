user_digit = input("Введите целое число 'n':\n>>>")

user_digit_double = user_digit + user_digit
user_digit_triple = user_digit + user_digit + user_digit
user_digit = int(user_digit)
user_digit_double = int(user_digit_double)
user_digit_triple = int(user_digit_triple)
summ = user_digit + user_digit_double + user_digit_triple

print("Сумма чисел 'n + nn + nnn' равна: ", summ)
