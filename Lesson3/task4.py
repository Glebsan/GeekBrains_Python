# Через **
def my_func(x, y):
    return x ** y


# Через цикл кривенько
def my_func2(x, y):
    i = y
    answer = 1
    while i < 0:
        answer *= x
        i += 1
    return 1 / answer


num1 = float(input())
num2 = int(input())

print('через **', my_func(num1, num2))
print('через числ', my_func2(num1, num2))
