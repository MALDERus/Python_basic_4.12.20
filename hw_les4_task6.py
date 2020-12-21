"""
Практическое задание 4.6 А
"""

from itertools import count
user_number = int(input("Введите стартовое число\n>>>"))
for el in count(user_number):
    if el > (user_number * 10):
        break
    else:
        print(el)

"""
Практическое задание 4.6 Б
"""

from itertools import cycle
current_list = [1, 2, 3, 4.5, True, "Los", [3, 2, 1]]
count = 1
for el in cycle(current_list):
    if count > 10:
        break
    print(el)
    count += 1