import os
file_path = os.path.join(os.path.dirname(__file__), "data.txt")


def count_words():
    with open(file_path, "r", encoding="UTF-8") as file:
        line_num = 1
        for line in file:
            words = line.split()
            print(f"Количество слов в строке номер {line_num}: {len(words)}")
            line_num += 1


def count_lines():
    with open(file_path, "r", encoding="UTF-8") as file:
        lines = 0
        for line in file:
            lines += 1
        print(f"Количество строк в файле: {lines}")


count_lines()
count_words()
