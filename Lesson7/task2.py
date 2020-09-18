from abc import ABC, abstractclassmethod


class Clothes(ABC):
    def __init__(self, name):
        self.name = name

    @abstractclassmethod
    def cloth_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    @property
    def cloth_consumption(self):
        return f'Расход ткани на {self.name} {self.size / 6.5 + 0.5}'


class Jacket(Clothes):
    def __init__(self, name, height):
        super().__init__(name)
        self.height = height

    @property
    def cloth_consumption(self):
        return f'Расход ткани на {self.name} {self.height * self.height + 0.3}'




coat = Coat('пальто', 6.5)
jacket = Jacket('костюм', 2)
print(coat.cloth_consumption)
print(jacket.cloth_consumption)
# print(jacket.cloth_consaption)
# print(total.total_consaption)
