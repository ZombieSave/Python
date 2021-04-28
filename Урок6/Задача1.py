import time


class TrafficLight:
    def __init__(self):
        self.__color = [31, 33, 32]

    def running(self):
        i = 0
        k = 1

        while True:
            print(f"\033[7m\033[{self.__color[i]}m")

            if i == 0:
                time.sleep(7)
                k = 1
            elif i == 1:
                time.sleep(2)
            elif i == 2:
                time.sleep(3)
                k = -1

            i += k


tl = TrafficLight()
tl.running()
