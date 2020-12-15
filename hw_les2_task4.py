user_string = input("Введите строку из нескольких слов, разделенных пробелами\n>>>")
user_string = user_string.split()

for index, el in enumerate(user_string, 1):
    if len(el) > 10:
        print(index, el[0:10])
        continue
    else:
        print(index, el)
