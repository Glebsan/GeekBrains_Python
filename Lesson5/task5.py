with open('set_of_numbers', 'w', encoding='UTF-8') as txt:
    num = input()
    txt.write(num + ' числа ' + '\n')
    summa = sum([int(i) for i in num.split()])
    txt.write(str(summa) + ' сумма чисел ')

print('Сумма чисел:', summa)
