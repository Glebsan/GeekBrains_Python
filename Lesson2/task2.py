elements_count = int(input())
list1 = []
answ = []
for i in range(elements_count):
    a = input()
    list1.append(a)

# Решение через пустой список
for i in range(1, elements_count, 2):
    answ.append(list1[i])
    answ.append(list1[i - 1])

if elements_count % 2 == 1:
    answ.append(list1[len(list1) - 1])
print('Оригнал:')
print(list1)
print('Решение через пустой список:')
print(answ)

# Решение через замену элементов в исходном списке
for i in range(1, elements_count, 2):
    list1[i], list1[i - 1] = list1[i - 1], list1[i]
print('Решение через замену элементов в исходном списке:')
print(list1)
