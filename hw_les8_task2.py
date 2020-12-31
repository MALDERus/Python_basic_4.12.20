class OopsDivisionByZero(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    devidend = int(input('Введите число, которое собираетесь разделить: '))
    division = int(input('Введите число, НА которое собираетесь разделить: '))
    if not division:
        raise OopsDivisionByZero('Деление на НОЛЬ!')
    print(f'Результат {devidend/division}')

except ValueError:
    print('вы ввели не числа')
except OopsDivisionByZero as error:
    print(error)
