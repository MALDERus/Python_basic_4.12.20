def int_function(str):
    return str.title()

print(int_function(input("Введите слово\n>>>")))

def int_function2(list):
    return " ".join(map(int_function, list.split()))

print(int_function2(input("Введите слова через пробел\n>>>")))