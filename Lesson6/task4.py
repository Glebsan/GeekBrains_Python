class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Car is going!')

    def stop(self):
        print('Car stopped!')

    def turn(self, direction):
        return 'Car turned to ' + direction

    def show_speed(self):
        print('Car speed', self.speed)

    def is_police_car(self):
        if self.is_police:
            return 'Police car'
        else:
            return 'Not police car'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print('Car speed is', self.speed)
        if self.speed > 60:
            return 'Speed is higher than 60'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print('Car speed', self.speed)
        if self.speed > 40:
            return 'Speed is higher than 40'

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)



my_town_car = TownCar(61, 'blue', 'BMW', False)
my_sport_car = SportCar(100, 'red', 'Skoda', False)
my_work_car = WorkCar(41, 'green', 'Lada', False)
my_police_car = PoliceCar(60, 'black', 'Ford', True)

print(my_town_car.turn('left'))
print(my_town_car.show_speed())
print(my_sport_car.speed, my_sport_car.color, my_sport_car.name, my_sport_car.is_police)
print(my_work_car.speed, my_work_car.color, my_work_car.name, my_work_car.is_police, my_work_car.show_speed())
print(my_police_car.speed, my_police_car.color, my_police_car.name, my_police_car.is_police, my_police_car.is_police_car())
