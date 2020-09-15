def my_func(name, surname, year, city, email, tel):
     return (name, surname, year, city, email, tel)

name = input('enter name: ')
surname = input('enter surname: ')
year = int(input('enter year: '))
city = input('enter city: ')
email = input('enter email: ')
tel = input('enter call number: ')

print(*my_func(name, surname, year, city, email, tel))
