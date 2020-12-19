"""
5. Реализовать расчет цены товара со скидкой.

Величина скидки должна передаваться в качестве аргумента в дочерний класс.

Выполнить перегрузку методов конструктора дочернего класса
(метод init, в который должна передаваться переменная — скидка),
и перегрузку метода str дочернего класса.

В этом методе должна пересчитываться цена и возвращаться результат —
цена товара со скидкой.

Чтобы все работало корректно, не забудьте инициализировать дочерний
и родительский классы
(вторая и третья строка после объявления дочернего класса).
"""


class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price


class ItemDiscountReport(ItemDiscount):
    def __init__(self, name, price, discount):
        self.discount = discount
        self.__name = name
        self.__price = price

    @property
    def get_name(self):
        return self.__name

    @property
    def get_price(self):
        return self.__price

    def change_price(self, price):
        self.__price = price

    def get_parent_data(self):
        print(f'name: {self.get_name}, price: {self.get_price}')

    def __str__(self):
        return f'Цена товара со скидкой: {str(self.__price - self.discount)}'


item = ItemDiscountReport('blablalba', 234, 10)
item.get_parent_data()
item.change_price(222)
item.get_parent_data()
print(item)
