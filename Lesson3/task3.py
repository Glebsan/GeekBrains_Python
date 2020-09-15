def my_func(a, b, c):
    answ = []
    my_list = [a, b, c]
    answ.append(max(my_list))
    my_list.remove(max(my_list))
    answ.append(max(my_list))
    return sum(answ)


num1 = int(input('1st number: '))
num2 = int(input('2nd number: '))
num3 = int(input('3nd number: '))

print(my_func(num1, num2, num3))
