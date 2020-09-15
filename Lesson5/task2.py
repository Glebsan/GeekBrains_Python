with open('input_text.txt') as txt:
    print('Кол-во строк:', len(txt.readlines()))
    txt.seek(0)
    num_of_line = 0
    for i in txt.readlines():
        num_of_line += 1
        print(f'Кол-во слов в {num_of_line} строке: {len(i.split())}')
