# 23. Найти сумму чисел списка, стоящих на нечетной позиции

# from random import randint

# def get_list(n, frst, last):
#     return [randint(frst, last) for i in range(n)]

# def sum_odd_position(my_list):
#     return sum(my_list[1::2])

# n = 10
# frst = 1
# last = 10

# my_list = get_list(n, frst, last)
# print(my_list)
# print(sum_odd_position(my_list))

# Улучшение кода:

import Func_list_generation as lg
numbers_list = lg.list_generation()
sum_odd = sum(numbers_list[item] for item in range(1, len(numbers_list), 2))
odd_el = str([numbers_list[item] for item in range(1, len(numbers_list), 2)]).strip('[]')
print(f'Для списка {numbers_list} сумма чисел, стоящих на нечётных позициях: \n{odd_el} равна {sum_odd}.')