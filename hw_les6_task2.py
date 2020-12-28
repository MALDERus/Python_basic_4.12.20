class Road:
    _massper1sqm = 25
    _thick = 5
    def __init__(self, lenght, width):
        self._lenght = int(lenght)
        self._width = int(width)


    def mass(self):
        return self._lenght * self._width * self._massper1sqm * self._thick

a = Road(5000, 20)
print(a.mass())
