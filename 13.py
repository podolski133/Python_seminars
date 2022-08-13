# 13. Для натурального n создать словарь индекс-значение, состоящий из элементов 
# последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# from random import randint

# def get_dict(n):
#     return {x: 3 * x + 1 for x in range(1, n+1)}

# n = randint(5, 20)

# print(n)
# print(get_dict(n))

# Улучшение кода:

sequence = '3*x+1'
n = int(input('Количество элементов словаря: '))
d = {x: eval(sequence) for x in range(1, n+1)}
print(f'для {n = }: {d}')