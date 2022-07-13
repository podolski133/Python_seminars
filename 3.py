# Вывести на экран числа от -N до N

n = int(input('Введите число n = '))
if n < 0:
    n = -n
for i in range(-n, n + 1):
    print(i)