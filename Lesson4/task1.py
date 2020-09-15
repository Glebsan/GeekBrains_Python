from sys import argv

hours, rate, prize = map(float, argv[1:]) #сам не додумался. Взял из Вашего решения

answ = hours * rate + prize
print('Hours:', hours)
print("rate:", rate)
print('prize:', prize)
print('Answer: ', answ)
