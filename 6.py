# Дано число обозначающее день недели. Вывести его название и указать является ли он выходным.

# 1 вариант:

# n = int(input('Введите число обозначающее день недели = '))
# if n == 1: print('Понедельник - будни')
# elif n == 2: print('Вторник - будни')
# elif n == 3: print('Среда - будни')
# elif n == 4: print('Четверг - будни')
# elif n == 5: print('Пятница - будни')
# elif n == 6: print('Суббота - выходной')
# elif n == 7: print('Воскресенье - выходной')
# else: print('Введено не корректное число')

# 2 вариант:

a = int(input('Введите число от 1 до 7: '))
week = ['mon', 'thue', 'wedn', 'thur', 'fri', 'sat', 'sun']
if a in range(1, 8):
    if a in range(1, 5):
        print(week[a - 1], '- будний день')
    else:
        print(week[a - 1], '- выходной день')
else:
    print('такого дня недели нет')