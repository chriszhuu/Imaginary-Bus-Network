from town import Town
from person import Person
from bus import Bus

townfile = open("town.txt","r")
townList = []
for aline in townfile.readlines():
    values = aline.split()
    townList.append(Town(values[1], values[3:])) # create Town objects and add to list


busfile = open("bus.txt","r")
busList = []
for aline in busfile.readlines():
    values = aline.split()
    busList.append(Bus(values)) # create Bus objects and add them to list

personfile = open("person.txt","r")
personList = []
for aline in personfile.readlines():
    values = aline.split()
    personList.append(Person(values[0], values[1], values[2]))
    # create Person objects and add them to list


# change person.origin and person.destination into town objects
for person in personList:
    for town in townList:
        if person.locate() == town.getName():
            person.setLocation(town)
        if person.getDestination() == town.getName():
            person.setDestination(town)

# change items in bus.route list into town objects
for n in range(len(busList[1].getRoute())):
    for bus in busList:
        for town in townList:
            if bus.getRoute()[n] == town.getName():
                bus.setRoute(n,town)

# after person & bus objects are created, add them to their respective town
for town in townList:
    town.locatePeople(personList)
    town.locateBus(busList)



def checkRoute():
    '''Check the legitimacy of bus routes: do they travel on existing roads?'''
    for n in range(2):
        for bus in busList:
            for town in townList:
                if bus.getRoute()[n] == town.getName()\
                   and bus.getRoute()[n + 1] not in town.getNeighbor():
                    print(">>> Warning: Bus", str(bus.getID()), "goes off the road.")
                    return False
    print("All bus routes have been checked. They don't go off the road.")
    return True


def pplInTown():
    '''this prints who is currently in which town'''
    for town in townList:
        town.printPplState()


def busState():
    '''prints passengers on board and the next stop for each bus'''
    for bus in busList:
        bus.printState()


def busLocate():
    '''this prints each bus's location'''
    for bus in busList:
        print("#"+str(bus.getID()),"is in",bus.locate())


def onetrip():
    '''this conducts one trip: passengers get on, buses drive'''
    for bus in busList:
        for n in range(len(bus.locate().getPeople())):
            bus.locate().getPeople()[n].getOn(bus)
        bus.drive()


def getOff():
    '''this ends a trip: passengers get off'''
    for person in personList:
        person.getOff(person.getBus())


def checkArrival():
    arrived = []
    for person in personList:
        if person.locate() == person.getDestination():
            arrived.append(person)
    if arrived == personList:
        print("*** All passengers have gotten to their destinations ***")
    else:
        print("*** Not everyone has gotten to their destinations ***")


def back_up():
    outfile = open("backup.txt","w")
    for person in personList:
        outfile.write(person.recordState() + "\n")
    for bus in busList:
        outfile.write(bus.recordState() + "\n")
    for town in townList:
        outfile.write(town.recordState() + "\n")


def read_back_up():
    '''this function allows backup file to input string attributes to each person
       and bus, then it changes those string attributes into town objects'''
    personList.clear()
    busList.clear()
    townList.clear()
    # create objects whose attributes reflect the current state of the system
    infile = open("backup.txt","r")
    for aline in infile.readlines():
        values = aline.split()
        if values[0] == "Person":
            personList.append(Person(values[3],values[7],values[5],values[9]))
        if values[0] == "Bus":
            busList.append(Bus(values[4:7],int(values[8]),int(values[10]),values[12:]))
        if values[0] == "Town":
            townList.append(Town(values[1],values[2:]))

    # change person.origin and person.destination into town objects
    for person in personList:
        for town in townList:
            if person.locate() == town.getName():
                person.setLocation(town)
                if person.getBus() == "None":
                    town.addPeople(person) # add ppl who are not on bus to town.peoplelist
            if person.getDestination() == town.getName():
                person.setDestination(town)
        # change each person's bus information from string into bus object
        if person.getBus() == "None":
            person.setBus(None)
        else:
            personOnBus = int(person.getBus())
            # cannot use int(person.getBus()) in "for" loop because person.getBus()
            # ceases to be a string at one point and there will be an error in loop
            for bus in busList:
                if bus.getID()-12 == personOnBus:
                # subtract 12 because 12 bus objects have been created before
                    person.setBus(bus)

    # change items in bus.route list into town objects
    for n in range(len(busList[0].getRoute())):
        for bus in busList:
            for town in townList:
                if bus.getRoute()[n] == town.getName():
                    bus.setRoute(n,town)
    # change items in bus.peopleList list into person objects
    for bus in busList:
        if bus.getPeople() is not None:
            for n in range(len(bus.getPeople())):
                for person in personList:
                    if bus.getPeople()[n] == person.getName():
                        bus.getPeople()[n] = person
    # add buses to respective towns
    for town in townList:
        town.locateBus(busList)


print(" ")
print(" ")

# display town, bus, passenger information
print(">>> There are twelve towns in this system... \n")
for town in townList:
    print(town.getName()+", connected to",town.getNeighbor())
print(" ")
print(" ")

for bus in busList:
    print(bus)
print(" ")
print(" ")

for person in personList:
    print(person.getName() + " wants to go from "+ person.locate().getName()
          + " to " + person.getDestination().getName() + ".")

print(" ")
print(" ")

print(">>> System check...\n")

checkRoute()

print(" ")
print(" ")

print(">>> At the beginning...\n")

pplInTown()  # prints who's in which town

print(" ")
print(" ")

print(">>> Starting the 1st trip...\n")

onetrip()  # passengers choose their bus for trip 1
busState()  # prints each bus's passengers on board and the next stop

print(" ")
print(" ")

back_up() # backing up the current state of bus system
read_back_up() # >>>>>> you can call these backup functions whenever you like <<<<<<<
               # tho these functions will bump up the bus IDs by 12 each time

print(">>> End of the first trip...\n")

getOff()  # passengers get off
pplInTown()  # prints who's in which town

print(" ")
print(" ")

print(">>> Starting the 2nd trip...\n")

onetrip()  # passengers choose their bus for trip 2
busState()  # prints each bus's passengers on board and the next stop

print(" ")
print(" ")

print(">>> End of the 2nd trip...\n")

getOff()
pplInTown()
checkArrival() # print whether all passengers have arrived at destination

print(" ")
print(" ")


