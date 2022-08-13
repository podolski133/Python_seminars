# 44. Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

# my_list = [1, 2, 3, 5, 1, 5, 3, 10]

# def get_unic(my_list):
#     unic = []
#     for i in range(len(my_list)):
#         if my_list[i] not in my_list[i+1::] and my_list[i] not in my_list[:i-1:]:
#             unic.append(my_list[i])
#     return unic

# print(get_unic(my_list))

# Улучшение кода:

import Func_list_generation as lg
numbers_list = lg.list_generation()
result_list = list(filter(lambda a: numbers_list.count(a) == 1, numbers_list))
print(f'Для последовательности {numbers_list}, \n   список уникальных элементов => {result_list}')