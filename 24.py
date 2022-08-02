# 24. Найти произведение пар чисел в списке.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from random import randint
import math

def get_numbers(n, frst, last):
    return [randint(frst, last) for i in range(n)]

def mult_pairs(my_list):
    return [my_list[i] * my_list[-i - 1] for i in range(math.ceil(len(my_list)/2))]

n = 9
frst = 1
last = 10

my_list = get_numbers(n, frst, last)
print(my_list)
print(mult_pairs(my_list))