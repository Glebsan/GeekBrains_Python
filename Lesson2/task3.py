n = int(input('Введите номер месяца: '))

# # Решение через лист (хотя больше через if)
season_list = ['winter', 'summer', 'autumn', 'spring']

if n == 12 or 1 or 2:
    print(season_list[0])
elif n == 3 or 4 or 5:
    print(season_list[3])
elif n == 6 or 7 or 8:
    print(season_list[1])
elif n == 9 or 10 or 11:
    print((season_list[2]))
else:
    print('Error')


# Еще через список и if )
season_list_2 = [[1, 2, 12], [3, 4, 5], [6, 7, 8], [9, 10, 11]]

if n in season_list_2[0]:
    print('winter')
elif n in season_list_2[1]:
    print('spring')
elif n in season_list_2[2]:
    print('summer')
elif n in season_list_2[3]:
    print('autumn')
else:
    print('Error')

# Решение через словарь
dict_ = {12: 'winter', 1: 'winter', 2: 'winter', 3: 'spring', 4: 'spring', 5:'spring', 6: 'summer', 7:'summer', 8: 'summer', 9: 'autumn', 10: 'autumn', 11: 'autumn' }

print(dict_[n])

