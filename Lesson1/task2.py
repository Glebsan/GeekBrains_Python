user_input = int(input('Enter value: '))

seconds = user_input % 60
minutes = user_input // 60 % 60
hours = user_input // 60 // 60

print(f'{hours}:{minutes}:{seconds}')
