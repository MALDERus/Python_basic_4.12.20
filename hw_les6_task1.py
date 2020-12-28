import time


class TrafficLight:
    __color = ("red", "yellow", "green")
    __time = (7, 2, 5)

    def running(self):
        for itm in zip(self.__color, self.__time):
            print(f"{itm[0]} light on, wait {itm[1]} sec.")
            time_count = itm[1]
            for i in range(time_count):
                print('%d sec remaining' % (time_count - i))
                time.sleep(1)


a = TrafficLight()
a.running()
