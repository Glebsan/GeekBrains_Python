a = int(input('Первый день: '))
b = int(input('Не менее: '))
count = 1
while a < b:
    a *= 1.1
    count += 1

print(f'Ответ: на {count}-й день спортсмен достиг результата — не менее {b} км.')
