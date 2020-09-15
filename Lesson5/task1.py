with open('input_text.txt', 'w') as f:
    i = input()
    while i != '':
        f.write(i + '\n')
        i = input()
