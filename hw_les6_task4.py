class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"Car {self.name} started moving")

    def stop(self):
        print(f"Car {self.name} stopped")

    def turn(self, direction):
        print(f"Car {self.name} turned {direction}")

    def show_speed(self):
        print(f"Car speed is {self.speed}")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'Warning! Speeding limit {self.speed}'
        else:
            return self.speed


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'Warning! Speeding limit {self.speed}'
        else:
            return f"Car speed is {self.speed}"


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police is True:
            return f'Police car'


car = TownCar(100, 'red', 'mazda', False)
car.go()
print(car.show_speed())
car.stop()
print(car.color)
print(car.is_police)

car_2 = PoliceCar(50, 'black', 'ford', True)
print(car_2.police())
print(car_2.name)
print(car_2.color)
car_2.go()
car_2.turn("right")
car_2.show_speed()
car_2.stop()

car_3 = SportCar(170, 'yellow', 'ferrari', False)
print(car_3.color)
print(car_3.name)
print(car_3.is_police)
car_3.show_speed()
car_3.turn("left")

car_4 = WorkCar(30, 'white', 'fiat', False)
car_4.go()
print(car_4.show_speed())
car_4.stop()
print(car_4.color)
print(car_4.is_police)
