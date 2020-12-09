user_seconds_count = input("Введите время в секундах:\n>>>")

if user_seconds_count.isdigit():
    user_seconds_count = int(user_seconds_count)
else:
    print("Ошибка ввода количества секунд, введите целое число")
    exit()

hours = user_seconds_count // 3600
minutes = (user_seconds_count - hours * 3600) // 60
seconds = user_seconds_count % 60
print(f"В формате 'чч:мм:сс' получаем: {hours}:{minutes}:{seconds}")
