class Bus(object):
    num = 0

    def __init__(self, route, index = 0, capacity = 3, peopleList = None):
        self.ID = Bus.num # automatically assign ID
        self.route = route # route is a list
        self.index = index  # index of the bus's location in self.route
        if peopleList is None:
            self.peopleList = []
        else:
            self.peopleList = peopleList # list of passengers on board
        self.capacity = capacity
        self.currentState = ''
        Bus.num = Bus.num + 1

    def getID(self):
        return self.ID

    def getRoute(self):
        return self.route

    def setRoute(self,index,town):
        self.getRoute()[index] = town

    def getIndex(self):
        return self.index

    def locate(self): # returns current location
        return self.getRoute()[self.index]

    def getDestination(self): # returns bus's remaining stops
        return self.getRoute()[self.index+1:]

    def getPeople(self):
        return self.peopleList

    def countPeople(self):
        return len(self.peopleList)

    def addPeople(self,person):
        self.getPeople().append(person)

    def removePeople(self,person):
        self.getPeople().remove(person)

    def getCapacity(self):
        return self.capacity

    def __str__(self):
        return "Bus # "+str(self.getID())+" goes from "+str(self.getRoute()[0])\
               +" to "+str(self.getRoute()[1])+" to "+str(self.getRoute()[2])

    def __repr__(self):
        return "Bus #"+str(self.getID())

    def isFull(self):
        if self.countPeople() == self.capacity:
            return True
        else:
            return False

    def drive(self):
        '''after passengers get on, this updates many fields as the bus drives to the next stop'''
        if self.getIndex() == len(self.route)-1:
            print("Bus has arrived at the final stop.")
        else:
            # remove people who just got on from the town.people list
            for person in self.getPeople():
                if person in self.getPeople() and person in self.locate().getPeople():
                    self.locate().removePeople(person)
            self.locate().removeBus(self) # remove bus from the current town
            self.index += 1 # updates bus location
            self.locate().addBus(self) # add bus to the town it's driving to
            for person in self.peopleList:
                person.setLocation(self.locate()) # updates location of all passengers

    def printState(self):
        '''prints passengers on board and the next stop'''
        if len(self.getPeople()) == 0:
            print("* Bus", str(self.getID()), "is empty, driving to",self.locate())
        elif len(self.getPeople()) == 1:
            print(self.getPeople(), "is on bus #"+ str(self.getID()),"to",self.locate())
        else:
            print(self.getPeople(), "are on bus #"+ str(self.getID()),"to",self.locate())

    def recordState(self):
        self.currentState = ''
        self.currentState += "Bus # " + str(self.ID) + " has_route " + str(self.getRoute()[0])\
                             + " " + str(self.getRoute()[1]) + " " + str(self.getRoute()[2])
        self.currentState += " Current_location_index: " + str(self.getIndex())
        self.currentState += " Capacity: " + str(self.getCapacity())
        self.currentState += " Current_passengers "
        for person in self.getPeople():
            self.currentState += person.getName() + " "
        return self.currentState