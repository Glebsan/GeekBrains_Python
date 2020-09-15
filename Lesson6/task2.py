class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asfalt_covering(self):
        self.mass = 25
        self.tickness = 0.05
        answer = self._length * self._width * self.mass * self.tickness / 1000
        print(f'Нужно {answer} т')


road = Road(5000, 20)
road.asfalt_covering()
