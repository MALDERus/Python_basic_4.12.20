current_list = [8, 3, 2, 5, 6, 7, 6, 9, 1]
new_list = [el for index, el in enumerate(current_list) if index and el > current_list[index - 1]]

print(new_list)
