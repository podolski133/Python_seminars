# 20. Реализуйте алгоритм задания случайных чисел без использования 
# встроенного генератора псевдослучайных чисел.

# import time

# a = str(time.time())
# b = a[-1] + a[-2]
# print(int(b))

# 2 вариант:
import time

def find_num(x):
    a = str(time.time())
    b = ''
    count = 1
    while count <= x:
        b += a[-count]
        count += 1
    return int(b)
print(find_num(3))