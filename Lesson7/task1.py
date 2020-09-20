class Matrix:
    def __init__(self, list1):
        self.list1 = list1
        # self.list2 = list2

    def __str__(self):
        for i in range(len(self.list1)):
            print(*self.list1[i])
        return ''  # костыль от NoneType ошибки =(

    def __add__(self, other):
        a = []
        b = []
        for i in range(len(self.list1)):
            for j in range(len(self.list1[i])):
                 a += ([self.list1[i][j] + other.list1[i][j]])
            b.append(a)
            a = []
        for i in b:
            print(*i)
        return '' # костыль от NoneType ошибки =( кажется это дич, подскажите как сделать по-другому!


test1 = Matrix([[31, 22], [37, 43], [51, 86]])
test2 = Matrix([[3, 5], [2,4], [1 , 64]])
print(test1)
print(test2)
print(test1 + test2)
print('qwe')

