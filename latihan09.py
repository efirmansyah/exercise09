class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    def getFirstname(self):
        return self.firstname
    
    def getLastname(self):
        return self.lastname

class Pets(Person):
    def __init__(self, name, type):
        self.name = name 
        self.type = type 

    def getName(self):
        return self.name

    def getType(self):
        return self.type 


pp = Person(Person.getFirstname)
pp.getPetsByPerson()



