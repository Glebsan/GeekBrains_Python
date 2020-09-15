sample_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

answ = [sample_list[i] for i in range(1, len(sample_list)) if sample_list[i] > sample_list[i - 1]]

print(answ)
