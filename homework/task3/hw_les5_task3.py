import os
file_path = os.path.join(os.path.dirname(__file__), "staff_sal.txt")

with open(file_path, "r", encoding="UTF-8") as file:
    data_dict = {}
    for line in file:
        key, value = line.split()
        data_dict[key] = int(value)

low_sal = []
for key, value in data_dict.items():
    if value < 20000:
        low_sal.append(key)

print(f"Сотрудники с зарплатой менее 20000: {low_sal}")
print(f"Средняя зарплата сотрудников: {round(sum(data_dict.values()) / len(data_dict.values()), 2)}")
