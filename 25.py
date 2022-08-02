# 25. В заданном списке вещественных чисел найдите разницу 
# между максимальным и минимальным значением дробной части элементов

from random import uniform

def get_real_nums (n, frst, last):
    return [round(uniform(frst,last), 2) for i in range(n)]

def find_diff(my_nums):
    nums = [round(x - int(x), 2) for x in (my_nums)]
    return max(nums) - min(nums)

n = 5
frst = 1
last = 10
my_nums = get_real_nums(n, frst, last)

print (my_nums)
print(find_diff(my_nums))