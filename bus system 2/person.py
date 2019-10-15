class Person(object):
    num = 0

    def __init__(self, name, curtown, destination, onBus = None):
        self.ID = Person.num
        self.name = name
        self.curTown = curtown
        self.destination = destination
        self.onBus = onBus # indicates which bus this person is on
        self.currentState = ''
        Person.num = Person.num + 1

    def getName(self):
        return self.name

    def setLocation(self, town):
        self.curTown = town

    def locate(self):
        return self.curTown

    def setDestination(self, town):
        self.destination = town

    def getDestination(self):
        return self.destination

    def getBus(self):
        return self.onBus

    def setBus(self,bus):
        self.onBus = bus # update the bus this person is on

    def getID(self):
        return self.ID

    def isOnBus(self): # indicates if this person is on a bus
        if self.onBus is not None:
            return True
        else:
            return False

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def getOn(self, bus): # person chooses a bus for herself
        if bus.isFull():
            print("*** Bus",bus.getID(),"is full and cannot take on more passengers.")
            return
        if self.isOnBus() is False:
            if self.locate() == bus.locate() and self.getDestination() in bus.getDestination():
                bus.addPeople(self) # updates bus passenger list
                self.setBus(bus) # updates which bus this person is on

    def getOff(self,bus): # person gets off the bus, if she's taking one
        if self.isOnBus():
            self.setBus(None) # updates person.onBus status
            bus.removePeople(self) # remove person from bus passenger list
            self.locate().addPeople(self) # add person to town's people list

    def recordState(self):
        self.currentState = ''
        self.currentState += "Person # " + str(self.ID) + " " + self.name
        self.currentState += " Destination: " + self.getDestination().getName()
        self.currentState += " Currently_in " + self.locate().getName()
        if self.onBus is None:
            self.currentState += " On_bus None"
        else:
            self.currentState += " On_bus " + str(self.onBus.getID())
        return self.currentState