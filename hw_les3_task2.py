def user_data(name, surname, y_of_b, city, email, phone):
    """
    Функция принимает в себя следующие  именованные параметры и выводит строку
    :param name: Имя
    :param surname: Фамилия
    :param y_of_b: Год рождения
    :param city: Город проживания
    :param email: email
    :param phone: телефон
    :return: строка с параметрами
    """
    return (f"Имя: - {name}; "
            f"фамилия: - {surname}; "
            f"год рождения: - {y_of_b}; "
            f"город проживания: - {city}; "
            f"email - {email}; "
            f"телефон - {phone}")

user_info = user_data(name=input("Введите имя:\n>>>"),
          surname=input("Введите фамилию:\n>>>"),
          y_of_b=input("Введите год рождения:\n>>>"),
          city=input("Введите город проживания:\n>>>"),
          email=input("Введите email:\n>>>"),
          phone=input("Введите телефон:\n>>>"))

print(user_info)
