from itertools import count, cycle


# task sample_gen:
print('task a.')
num = int(input('Enter number: '))

for i in count(num):
    if i == 10:
        break
    print(i)

print()

# task b:
print('task b.')
sample_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

sample_gen = cycle(sample_list)

while True:
    print(next(sample_gen))
    if input("Enter 'q' for exit: ").lower() == 'q':
        break
