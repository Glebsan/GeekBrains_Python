"""
6. Проверить на практике возможности полиморфизма.

Необходимо разделить дочерний класс ItemDiscountReport на два класса.

Инициализировать классы необязательно.

Внутри каждого поместить функцию get_info,
которая в первом классе будет отвечать за вывод названия товара,
а вторая — его цены.

Далее реализовать выполнение каждой из функции тремя способами.
"""

class ItemDiscount:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ItemDiscountReport_1(ItemDiscount):
    def get_info(self):
        print(self.name)


class ItemDiscountReport_2(ItemDiscount):
        def get_info(self):
            print(self.price)


# Первый способ
first = ItemDiscountReport_1('first', 20)
second = ItemDiscountReport_2('second', 30)


first.get_info()
second.get_info()

# Второй способ
def get_info(class_exaple):
    return class_exaple.get_info()

get_info(first)
get_info(second)

# Третий способ
for i in (first, second):
    i.get_info()
