# По моему пользовательское число добавляется не в конец одинаковых с ним чисел...

my_list = [7, 5, 3, 3, 2]
count = 0

inp = int(input('Enter number: '))

for i in my_list:
    if inp <= i:
        count += 1
        continue
    my_list.insert(count, inp)
    print(my_list)
    break
else:
    my_list.append(inp)
    print(my_list)
