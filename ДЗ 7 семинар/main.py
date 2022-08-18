import controller as mC
import our_DB as DB
from Person import Person as Person

actions={
    '1': 'Вывести список контактов',
    '2': 'Добавить контакт',
    '3': 'Удалить контакт',
    '4': 'Найти по имени',
    '0': 'Выйти из программы' }
def print_actions():
    for i in actions.items(): print(i)

exitKey=True
while (exitKey):
    print_actions()
    a = input('введите цифру действия: ')
    if a in actions:
        if a=='1': 
            listOfPeople=DB.getInfoFromFile()
            DB.showListOfPeople(listOfPeople)
        elif a=='2': 
            strPerson=input('введите данные нового человека через пробел (Фамилия, Имя, Отчество, возраст, телефон, описание): ')
            DB.recordNewPerson(strPerson)
        elif a=='3': 
            strName = input('введите имя для удаления из БД: ')
            DB.deletePerson(mC.findPersonForRemoval(strName))
        elif a=='4': 
            strName = input('введите имя для поиска в БД: ')
            mC.findPersonByName(strName)  
        elif a=='0': exitKey=False; print('Пока Пока')    
    else: print('нет такого значения')