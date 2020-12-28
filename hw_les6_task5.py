class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):
    def draw(self):
        print(f"Запуск отрисовки с помощью {self.title}")


class Pencil(Stationery):
    def draw(self):
        print(f"Запуск отрисовки с помощью {self.title}")


class Handle(Stationery):
    def draw(self):
        print(f"Запуск отрисовки с помощью {self.title}")


a = Pen("ручка")
a.draw()

a = Pencil("карандаш")
a.draw()

a = Handle("маркер")
a.draw()
