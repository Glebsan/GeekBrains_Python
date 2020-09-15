from math import factorial


def fact(x):
    for x in range(1, x + 1):
        yield factorial(x)


num = int(input('Enter number: '))

list_gen = enumerate([i for i in fact(num)], 1)

for i in list_gen:
    print('Factorial of', i[0], '=', i[1])
