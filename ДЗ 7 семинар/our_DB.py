import controller as mC
#import pandas as pd

nameOfTheDB = "PhoneBook.txt"

def getInfoFromFile():
    with open(nameOfTheDB, "r", encoding='utf-8') as file:
        fileData=file.readlines()
        listOfPeople=mC.listOfPeopleFromFile(fileData)       
    return listOfPeople

def showListOfPeople(listOfPeople):
    for i in range(len(listOfPeople)):
        print(listOfPeople[i].lastName, listOfPeople[i].name, listOfPeople[i].middleName, listOfPeople[i].age ,listOfPeople[i].phoneNumber, listOfPeople[i].description)
    print('')    

def recordNewPerson(data):
    with open(nameOfTheDB, "a", encoding='utf-8') as file:
        if len(data.split())<2: print('Ленивец, введи хотя бы фамилию  имя')
        else:
            file.writelines('\n')
            file.writelines(data)
            for i in range(len(data.split()), 6):
                file.writelines(' пусто')

def deletePerson(listOfPeople):
    list1=[]
    with open(nameOfTheDB, "w", encoding='utf-8') as file:
        for i in range(len(listOfPeople)):
            list1.append(listOfPeople[i].lastName); list1.append(' ')
            list1.append(listOfPeople[i].name); list1.append(' ')
            list1.append(listOfPeople[i].middleName); list1.append(' ')
            list1.append(listOfPeople[i].age); list1.append(' ')
            list1.append(listOfPeople[i].phoneNumber); list1.append(' ')
            list1.append(listOfPeople[i].description); 
            if i!= len(listOfPeople)-1: list1.append('\n')
            file.writelines(list1)  
            list1=[] 

def showPersonAfterSearch(person):
    print(person.lastName, person.name, person.middleName, person.age, person.phoneNumber, person.description)
    print('')