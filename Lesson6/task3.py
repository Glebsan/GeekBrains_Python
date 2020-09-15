class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def __init__(self, name, surname, position, profit, bonus):
        super().__init__(name, surname, position, profit, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_full_profit(self):
        return self._income.get('wage') + self._income.get('bonus')


my_position = Position('Vladimir', 'Putin', 'president', 20000, 94932)
print("Имя:", my_position.name)
print("Фамилия:", my_position.surname)
print("Должность:", my_position.position)
print("Оклад:", my_position._income.get('wage'))
print("Бонус:", my_position._income.get('bonus'))
print("Полное имя:", my_position.get_full_name())
print("Доход:", my_position.get_full_profit())
