from time import sleep


class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    @staticmethod  # это мне посоветовал сделать PyCharm. Видимо какой-то декоратор...
    def running():
        time = [7, 2, 1]
        while True:
            for i in range(len(TrafficLight.__color)):
                print(f'Цвет светофора:{TrafficLight.__color[i]}.Ждем {time[i]} сек.')
                sleep(time[i])


a = TrafficLight()
a.running()
