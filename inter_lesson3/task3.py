import itertools


keys = [1, 2, 3, 4, 5]
values = [6, 7, 8, 9, 10, 11]

dictionary = dict(itertools.zip_longest(keys, values[:len(keys)], fillvalue='None'))
print(dictionary)
