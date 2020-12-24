import os
file_path = os.path.join(os.path.dirname(__file__), "RuEn.txt")
ru_file_path = os.path.join(os.path.dirname(__file__), "EnRu.txt")

dictionary = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}

with open(file_path, "r", encoding="UTF-8") as file:
    content = file.read().splitlines()

with open(ru_file_path, "w", encoding="UTF-8") as file:
    count = 0
    for itm in content:
        if count < (len(content) - 1):
            data_tuple = itm.split()
            data_tuple[0] = dictionary[data_tuple[0]]
            file.write(' '.join(data_tuple) + "\n")
            count += 1
        else:
            data_tuple = itm.split()
            data_tuple[0] = dictionary[data_tuple[0]]
            file.write(' '.join(data_tuple))
