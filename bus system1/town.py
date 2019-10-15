class Town(object):
    all = [] # list of all objects in Town
    num = 0

    def __init__(self, name, neighbor):
        self.name = name
        self.neighbor = neighbor # neighbor is a list of neighboring towns
        self.ID = Town.num
        Town.num = Town.num + 1
        Town.all.append(self)

    def getNeighbor(self):
        return self.neighbor

    def getName(self):
        return self.name

    def getID(self):
        return self.ID

    def __str__(self):
        return str(self.name)




