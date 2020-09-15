n = int(input('Enter num: '))
m = n % 10

while n > 0:
    if m < n % 10:
        m = n % 10
    n //= 10

print('Наибольшая цифра в числе:', m)
