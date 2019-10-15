class Person(object):
    travelling = [] # list of Person objects who still needs to travel
    arrived =[] # list of Person objects that have arrived at the destination
    num = 0

    def __init__(self, name, origin, destination):
        self.ID = Person.num # automatically assign ID
        self.name = name
        self.origin = origin
        self.destination = destination
        Person.num = Person.num + 1
        Person.travelling.append(self)
        self.places = [self.origin] # a list of where the person has been


    def getName(self):
        return self.name

    def getOrigin(self):
        return self.places[0] # the starting point of each person

    def getDestination(self):
        return self.destination

    def getID(self):
        return self.ID

    def __str__(self):
        return self.name + " wants to go from "+ self.places[0] + " to " + self.destination + "."

    def locate(self):
        return self.places[len(self.places)-1] # the last item on the list "self.places"
                                               # i.e. current location


