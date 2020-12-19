import os


def file_name(path):
    file = os.path.abspath(path)
    return os.path.splitext(os.path.basename(file))[0]


print(file_name('task1'))
