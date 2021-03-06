# Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.  

## N = 5 - это кол-во числа последовательности 
## (умножение с 1 на -3 каждое последующее число)

# 1 вариант

def search_number(a, b):
    my_list = [1] # 1. берется значение изначально  1 в списке лежит
    while len(my_list) < a: # 2. Пока длина списка меньше чем заданное пользователем кол-во членов
        my_list.append(my_list[-1]*b) # 3. Мы берем элемент последний из нашего списка и умножаем на множитель, по умолчанию -3
    print(my_list)
search_number(5, -3)

# append - добавление нового элемента в конец списка

# 2 вариант

# def func(x):
#     s = 1
#     print(s, end=' ')
#     for i in range(1,x):
#         s = s * -3
#         print(s, end=' ')

# n = int(input('Введите число: '))
# func(n)

# Улучшенный вариант 1 варианта:

# def search_number(a: int, b: int) -> list: ## Type Hinting - это механизм, который позволяет явно указывать типы параметров.
#     my_list = [1]
#     i = 1
#     while len(my_list) < a:
#         my_list.append(my_list[i-1]*b) # 3. Мы берем элемент последний из нашего списка и умножаем на множитель, по умолчанию -3
#         i += 1
#     return my_list
# print(search_number(5, -3))