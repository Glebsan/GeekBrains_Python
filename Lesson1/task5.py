earnings = int(input('Выручка: '))
costs = int(input('Издержки: '))

if earnings - costs <= 0: # ноль считаю убытком =)
    print('Убыток')
else:
    print('Прибыль')
    profit = earnings - costs
    print(f'Рентабельность выручки: {profit / costs}')
    staff = int(input('Кол-во сотрудников: '))
    print('Прибыль на одного сотрудника: ', profit / staff )
