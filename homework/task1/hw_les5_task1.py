import os
file_name = "user_text.txt"
file_path = os.path.join(os.path.dirname(__file__), f"{file_name}")

with open(file_path, "w", encoding="UTF-8") as file:
    while True:
        user_data = (input("Введите данные:\n>>>"))
        if not user_data:
            break
        file.write(f"{user_data}\n")
