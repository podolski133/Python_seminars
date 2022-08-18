from Person import Person as Person
import our_DB as DB

def listOfPeopleFromFile(data):
    listOfPeople = []
    descr = ''
    for i in range(len(data)):
        personTemp = data[i].split()
        for j in range(5,len(personTemp)):
            descr += personTemp[j] + ' '
        person = Person(personTemp[0],personTemp[1],personTemp[2],personTemp[3],personTemp[4], descr)
        descr = ''
        listOfPeople.append(person)
    return listOfPeople

def createNewPerson(data):
    personTemp = data.split()    
    person = Person(personTemp[0],personTemp[1],personTemp[2],personTemp[3],personTemp[4], personTemp[5])
    return person    

def findPersonByName(strName):    
    listOfPeople=DB.getInfoFromFile()
    counter=0
    for i in range(len(listOfPeople)):
        if listOfPeople[i].name == strName: DB.showPersonAfterSearch(listOfPeople[i])
        counter+=1
    if counter==0: print('В БД нет таких имен')

def findPersonForRemoval(strName):
    listOfPeople=DB.getInfoFromFile()
    counter=0; list1=[]
    for i in range(len(listOfPeople)):
        if listOfPeople[i].name == strName: 
            counter+=1; 
            list1.append(i)
    if counter==0: print('В БД нет пригодных контактов для удаления')
    else:
        list1.reverse()
        for i in range(len(list1)):
            listOfPeople.pop(list1[i])      
    return listOfPeople        

def serviceForChecking(listOfPeople):
    list1=[]
    for i in range(len(listOfPeople)):
            list1.append(listOfPeople[i].lastName); list1.append(' ')
            list1.append(listOfPeople[i].name); list1.append(' ')
            list1.append(listOfPeople[i].middleName); list1.append(' ')
            list1.append(listOfPeople[i].age); list1.append(' ')
            list1.append(listOfPeople[i].phoneNumber); list1.append(' ')
            list1.append(listOfPeople[i].description); list1.append('\n')
            print(list1)  
            list1=[]     