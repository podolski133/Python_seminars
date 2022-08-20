import pandas as pd


def logger_add_puple():
    data = pd.read_csv('puples.csv')
    add_data = \
        {
            'Имя': [input('Введите имя ученика: ')],
            'Фамилия': [input('Введите фамилия ученика: ')],
            'Отчество': [input('Введите отчество ученика: ')],
            'Дата рождения': [input('Введите дату рождения ученика: ')],
            'Класс': [input('Введите класс ученика: ')],
            'Место': [input('Введите место ученика: ')],
            'Статус': [input('Введите статус ученика: ')],
        }
    add_data = pd.DataFrame(add_data)
    add_data.index += 1
    data = pd.concat([data, add_data], ignore_index=True)
    data.to_csv('puples.csv', index=False)


def logger_add_class():
    data = pd.read_csv('class.csv')
    add_data = \
        {
            'Место': [input('Введите № место: ')],
            'Кабинет': [input('Введите № кабинета: ')],
            'Ряд': [input('Введите № ряда: ')],
            'Парта': [input('Введите № парты: ')],
            'Вариант': [input('Введите № варианта: ')],
        }
    add_data = pd.DataFrame(add_data)
    add_data.index += 1
    data = pd.concat([data, add_data], ignore_index=True)
    data.to_csv('class.csv', index=False)


def find_data():
    menu = \
        {
            1: 'Поиск по имени',
            2: 'Поиск по фамилии',
            3: 'Поиск по отчеству',
            4: 'Поиск по дате рождения',
            5: 'Поиск по классу',
            6: 'Поиск по месту',
            7: 'Поиск по статусу',
            8: 'Поиск класса ученика'
        }
    tool = \
        {
            1: 'Имя',
            2: 'Фамилия',
            3: 'Отчество',
            4: 'Дата рождения',
            5: 'Класс',
            6: 'Место',
            7: 'Статус',
            8: 'Место'
        }

    for v, k in menu.items():
        print(f'{v}:{k}')

    operation = int(input('Введите номер операции: '))
    if operation !=8:
        if operation == 6:
            find_item = int(input(f'Введите {tool.get(operation).lower()} для поиска: '))
        else:
            find_item = input(f'Введите {tool.get(operation).lower()} для поиска: ')
        data = pd.read_csv('puples.csv')
        print(data.loc[data[tool.get(operation)] == find_item])
    else:
        data = pd.read_csv('class.csv')
        find_item = int(input(f'Введите {tool.get(operation).lower()} для поиска: '))
        print(data.loc[data[tool.get(operation)] == find_item])


def logger_del():
    data = pd.read_csv('puples.csv')
    operation = int(input('Введите номер записи для удаления: '))
    print(data.iloc[operation])
    accept = input('Подтвердите удаление. Да/Нет: ').lower()

    if accept == 'да':
        data = data.drop([operation], axis=0)
        print('Запись успешно удалена.')

    data.to_csv('puples.csv', index=False)



