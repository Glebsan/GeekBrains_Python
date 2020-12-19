
number = float(input('Enter num: '))
if number.is_integer():
    print('Целое')
else:
    print('Дробное')
    print(str(number).split('.')[0] == str(number).split('.')[1])
