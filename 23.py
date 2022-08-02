# 23. Найти сумму чисел списка, стоящих на нечетной позиции

from random import randint

def get_list(n, frst, last):
    return [randint(frst, last) for i in range(n)]

def sum_odd_position(my_list):
    return sum(my_list[1::2])

n = 10
frst = 1
last = 10

my_list = get_list(n, frst, last)
print(my_list)
print(sum_odd_position(my_list))