sample_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

answ = [i for i in sample_list if sample_list.count(i) < 2]

print(answ)
