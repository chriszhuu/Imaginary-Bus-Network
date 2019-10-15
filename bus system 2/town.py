class Town(object):
    num = 0

    def __init__(self, name, neighbor):
        self.name = name
        self.neighbor = neighbor # neighbor is a list of neighboring towns
        self.ID = Town.num
        self.busList = [] # list of buses currently in this town
        self.peopleList = [] # list of people currently in this town
        self.currentState = ''
        Town.num = Town.num + 1

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return str(self.name)

    def getName(self):
        return self.name

    def getNeighbor(self):
        return self.neighbor

    def getPeople(self):
        return self.peopleList

    def getBus(self):
        return self.busList

    def addPeople(self,person): # add people to this town
        self.peopleList.append(person)

    def removePeople(self,person): # remove people to this town
        self.getPeople().remove(person)

    def addBus(self,bus):
        self.busList.append(bus)

    def removeBus(self,bus):
        self.busList.remove(bus)

    def locatePeople(self, peoplelist): # add people to their respective town
        for person in peoplelist:
            if person.locate() is self:
                self.addPeople(person)

    def locateBus(self, buslist): # add buses to their respective town
        for bus in buslist:
            if str(bus.locate()) is self.getName():
                self.addBus(bus)

    def printPplState(self): # prints who is currently in this town
        if len(self.getPeople()) == 0:
            print("* Nobody is in", self.getName())
        elif len(self.getPeople()) == 1:
            print(self.getPeople(), "is in", self.getName())
        else:
            print(self.getPeople(), "are in", self.getName())

    def printBusState(self): # prints which bus is currently in this town
        if len(self.getBus()) == 0:
            print("* No bus is in", self.getName())
        elif len(self.getBus()) == 1:
            print(self.getBus(), "is in", self.getName())
        else:
            print(self.getBus(), "are in", self.getName())

    def recordState(self):
        self.currentState = 'Town '
        self.currentState += self.getName() + " "
        for item in self.getNeighbor():
            self.currentState += item + " "
        return self.currentState
