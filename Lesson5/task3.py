with open('employers.txt', encoding='UTF-8') as txt:
    average_salary = 0
    print('Заработная плата менее 20000:')
    for i in txt:
        a = i.split()
        average_salary += int(a[1])
        if int(a[1]) < 20000:
            print(*a)
    txt.seek(0)
    print('Средняя зарплата \'сотрудников\':', average_salary / len(txt.readline()))
