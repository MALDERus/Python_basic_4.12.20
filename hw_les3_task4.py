x = int(input("Введите действительное положительное число 'x'\n>>>"))
y = int(input("Введите целое отрицательное число 'y'\n>>>"))

# def my_func(x, y):
#     return x**y
#
# result = my_func(x, y)
#
# print(result)

def my_multip(x, y):
    result = 0
    for i in range(y):
        result += x
    return result

def my_func(x: float, y: int):
    result = 1
    for i in range(abs(y)):
        result = my_multip(result, x)
    return result if y > 0 else 1 / result

print(my_func(x, y))






