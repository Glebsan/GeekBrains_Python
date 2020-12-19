import os
import random
import string


def create_file(name):
    path = os.path.join('C:\\Users\\Glebs\\PycharmProjects\\pythonProject\\lesson3', name)


    if os.path.exists(path):
        print('File has already exists')
    else:
        with open(path, 'w', encoding='utf-8') as file:
            pass
        write_read(name)


def write_read(name):
    list_num = [random.randint(1, 10) for _ in range(5)]
    list_text = [random.choice(string.ascii_letters) for _ in range(3)]


    zip_list = list(zip(list_num, list_text))

    with open(name, 'w', encoding='utf-8') as file:
        for line in zip_list:
            file.write(str(line) + '\n')

    with open(name, 'r', encoding='utf-8') as file2:
        for line in file2.read():
            print(line, end='')

create_file('test.txt')
