from functools import reduce

def mult(prev_el, el):
    return prev_el * el

def fact(n):
    yield reduce(mult, range(1, n + 1))

n = int(input("Введите число n! для вывода факториалов чисел от 1 до n\n>>>"))

for el in range(1, n + 1):
    gen = fact(el)
    for el in gen:
        print(el)
