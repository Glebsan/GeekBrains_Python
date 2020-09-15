class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return 'Start drawing...'


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return 'Start drawing...by Pen'


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return 'Start drawing...by Pencil'


class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return 'Start drawing...by Handle'


my_stationary = Stationary('stationary!')
my_pen = Pen('Pen!')
my_pencil = Pencil('Pencil!')
my_handle = Handle('Handle!')

print(my_stationary.title, my_stationary.draw())
print(my_pen.title, my_pen.draw())
print(my_pencil.title, my_pencil.draw())
print(my_handle.title, my_handle.draw())
