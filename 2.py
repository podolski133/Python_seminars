# Найти максимальное из пяти чисел

# 1 вариант:

# a = int(input('Введите первое число = '))
# b = int(input('Введите второе число = '))
# c = int(input('Введите третье число = '))
# d = int(input('Введите четвертое число = '))
# e = int(input('Введите пятое число = '))
# if a>b and a>c and a>d and a>e:
#     print(f'Максимальное число {a}')
# elif b>a and b>c and b>d and b>e:
#     print(f'Максимальное число {b}')
# elif c>a and c>b and c>d and c>e:
#     print(f'Максимальное число {c}')
# elif d>a and d>b and d>c and d>e:
#     print(f'Максимальное число {d}')
# else: 
#     print(f'Максимальное число {e}')

# 2 вариант:

# a = int(input('Введите первое число = '))
# b = int(input('Введите второе число = '))
# c = int(input('Введите третье число = '))
# d = int(input('Введите четвертое число = '))
# e = int(input('Введите пятое число = '))
# max = a
# for i in [b,c,d,e]:
#     if max < i:
#         max = i
# print(f'Максимальное число = {max}')

# 3 вариант:

for i in range(1,6):
    a = int(input(f'Введите число {i}= '))
    if i == 1:
        max = a
    elif max < a:
        max = a
print(f'Максимальное число = {max}')
