from functools import reduce
new_list = [el for el in range(100, 1001) if (el % 2) == 0]

def mult(prev_el, el):
    return prev_el * el

print(reduce(mult, new_list))
