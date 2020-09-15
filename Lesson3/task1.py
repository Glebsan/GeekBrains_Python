def mod_(a, b):
    return a / b


a = int(input())
b = int(input())

if b == 0:
    print('Нельзя делить на 0.')
else:
    print(mod_(a, b))
