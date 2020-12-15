exchange_list = input("Веведите элементы списка разделяя их 'пробелом'\n>>>")
exchange_list = exchange_list.split()

for index_el in range(0, len(exchange_list) - 1, 2):
    exchange_list[index_el], exchange_list[index_el + 1] = exchange_list[index_el + 1], exchange_list[index_el]

print(exchange_list)
