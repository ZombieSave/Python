import time


class TrafficLight:
    def __init__(self):
        self.__color = [(31, 7), (33, 2), (32, 3)]

    def running(self):
        i = 0
        k = -1

        while True:
            print(f"\033[7m\033[{self.__color[i][0]}m")
            time.sleep(self.__color[i][1])

            if i == 0 or i == len(self.__color) - 1:
                k *= -1
                
            i += k