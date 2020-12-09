city_name = "New-Vasuki"
city_streets_count = 3

print(f"Название города: {city_name}, в этом городе {city_streets_count} улицы")

user_city_name = input("Введите название Вашего города:\n>>>")
user_city_streets_count = input("Введите количество улиц в Вашем городе:\n>>>")

if user_city_streets_count.isdigit():
    user_city_streets_count = int(user_city_streets_count)
else:
    print("Ошибка ввода количества улиц, введите число")
    exit()

print(f"Ваш город {user_city_name}, в нём {user_city_streets_count} улиц.")
