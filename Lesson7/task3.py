class Cell:
    def __init__(self, count):
        self.count = int(count)

    def __str__(self):
        return str(self.count)

    def __add__(self, other):
        return f'Результат сложения клеток: {self.count + other.count}'
    def __sub__(self, other):
        return f'Результат вычитания клеток: {self.count - other.count if self.count - other.count >= 0 else f"Отрицательное число"}'

    def __mul__(self, other):
        return f'Результат умножения клеток: {self.count * other.count}'

    def __truediv__(self, other):
        return f'Результат деления с округлением: {round(self.count / other.count)}'

    def make_order(self, cells_in_raw):
        print('Распределение по рядам:')
        for i in range(self.count // cells_in_raw):
            print(cells_in_raw * '*')
        print(self.count % cells_in_raw * '*')
        return ''


cell_1 = Cell(15)
cell_2 = Cell(10)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_2.make_order(3))
