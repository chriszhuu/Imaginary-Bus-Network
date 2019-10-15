class Bus(object):
    num = 0
    all = [] # list of all objects in Bus

    def __init__(self, route):
        self.ID = Bus.num
        self.route = route # bus route is a list with 3 items
        self.origin = route[0] # bus origin is the first item in the list
        self.destination = route[1:] # bus destinations are the remaining items
        self.curCap = 0 # current capacity
        self.capacity = 3
        Bus.num = Bus.num + 1
        Bus.all.append(self)
        self.curLoc = None # current location


    def getRoute(self):
        return self.route

    def getID(self):
        return self.ID

    def setCapacity(self,num):
        self.capacity = num

    def __str__(self):
        return "Route "+str(self.getID())+" bus starts from "+self.route[0]\
               +", goes to "+self.route[1]+" and "+self.route[2]

    def isFull(self):
        if self.curCap == self.capacity:
            return True
        else:
            return False

    def locate(self):
        return self.curLoc

    def passengerCount(self):
        return self.curCap



