"""
3. Усовершенствовать родительский класс таким образом,
чтобы получить доступ к защищенным переменным.
"""


class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def get_name(self):
        return self.__name

    @property
    def get_price(self):
        return self.__price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        print(f'name: {self.get_name}, price: {self.get_price}')


item = ItemDiscountReport('blablalba', 234)
item.get_parent_data()
