import os
file_path = os.path.join(os.path.dirname(__file__), "nums.txt")

try:
    with open(file_path, 'w+', encoding="UTF-8") as file:
        line = input('Введите цифры через пробел \n>>>')
        file.write(line)
        my_numb = line.split()
        print(sum(map(int, my_numb)))
except IOError:
    print('Ошибка в файле')
except ValueError:
    print('Вы ввели не число')
