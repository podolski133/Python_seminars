# 36. В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. 
# Найдите это число.

def get_data_from_file(nums):
    data = open(nums, 'r')
    dlist = data.read() + ' '
    dlist = list(map(int, dlist.split()))
    data.close()
    return dlist

def find_number(nums):
    for i in range(len(nums)-1):
        if nums[i+1] - nums[i] > 1:
            return nums[i] + 1


fnums = '36_file_test.txt'
nums_list = get_data_from_file(fnums)

print(nums_list)
print(find_number(nums_list))


# Добавить недостающее число в список

def get_full_nums(nums):
    for i in range(len(nums)-1):
        if nums[i+1] - nums[i] > 1:
            nums.insert(i+1, nums[i] + 1)
    return nums

nums = get_data_from_file(fnums)

print(get_full_nums(nums_list))