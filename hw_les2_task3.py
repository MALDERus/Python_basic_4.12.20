'''
Решение через список
'''

# user_month = int(input("Введите месяц в виде целого числа от 1 до 12\n>>>"))
#
# month_list = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
#
# if user_month in month_list[0:3]:
#     print("Winter")
# elif user_month in month_list[3:6]:
#     print("Spring")
# elif user_month in month_list[6:9]:
#     print("Summer")
# else:
#     print("Autumn")

'''
Решение через словарь
'''

user_month = int(input("Введите месяц в виде целого числа от 1 до 12\n>>>"))

month_dict = {12: "Winter", 1: "Winter", 2: "Winter",
              3: "Spring", 4: "Spring", 5: "Spring",
              6: "Summer", 7: "Summer", 8: "Summer",
              9: "Autumn", 10: "Autumn", 11: "Autumn"}

print(month_dict.get(user_month))
