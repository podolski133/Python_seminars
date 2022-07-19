# Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.  

## N = 5 - это кол-во числа последовательности 
## (умножение с 1 на -3 каждое последующее число)

def search_number(a, b):
    my_list = [1]
    while len(my_list) < a:
        my_list.append(my_list[-1]*b)
    print(my_list)
search_number(5, -3)