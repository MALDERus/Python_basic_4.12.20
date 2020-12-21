current_list = [1, 1, 2, 3, 3, 4, 5, 5, 6, 7, 7, 8, 9, 9]
new_list = [el for el in current_list if current_list.count(el) == 1]

print(new_list)
