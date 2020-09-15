
# для выхода ввести 'exit'
res = 0
flag = True
while flag:
    inp_ = input('Введите значение').split()
    for a in inp_:
        if a.lower() == 'exit':
            print(res)
            flag = False
            break
        res += int(a)
