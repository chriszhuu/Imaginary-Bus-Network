from bus import Bus
from town import Town
from people import Person


townfile = open("town.txt","r")
for aline in townfile.readlines():
    values = aline.split()
    Town(values[1], values[3:]) # create Town objects

busfile = open("bus.txt","r")
for aline in busfile.readlines():
    values = aline.split()
    Bus(values) # create Bus objects

personfile = open("person.txt","r")
for aline in personfile.readlines():
    values = aline.split()
    Person(values[0], values[1], values[2]) # create Person objects


# Town Info Display
print(">>> There are twelve towns in this system... \n")
for town in Town.all:
    print(town.getName()+", which is connected to",town.getNeighbor())
print(" ")
print(" ")


# Bus Info Display
for bus in Bus.all:
    print(bus)
print(" ")
print(" ")


# Passenger Info Display
for person in Person.travelling:
    print("Passenger", str(person.getID()+1),":", person)
print(" ")
print(" ")


def check_bus():
    '''Check the legitimacy of bus routes: do they travel on existing roads?'''
    for n in range(2):
        for bus in Bus.all:
            for town in Town.all:
                if bus.getRoute()[n] == town.getName():
                    if bus.getRoute()[n+1] not in town.getNeighbor():
                        print(">>> Warning: Bus",str(bus.getID()),"goes off the road.")
    print("... All bus routes have been checked. They don't go off the road.")
    return


def pplInTown():
    '''this prints the people currently in each town'''
    for town in Town.all:
        town.ppl = []
        for person in Person.travelling:
            # Person.travelling contains people still travelling
            if town.getName() == person.locate():
                town.ppl.append(person.getName())
        for person in Person.arrived:
            # Person.arrived contains people who have completed the trip
            if town.getName() == person.locate():
                town.ppl.append(person.getName())

        if len(town.ppl) == 0:
            print("* Nobody is in",town.getName())
        elif len(town.ppl) == 1:
            print(town.ppl,"is in",town.getName())
        else:
            print(town.ppl,"are in",town.getName())
    if len(Person.travelling) == 0:
        # additional sign if everyone has completely her trip
        print("*** All passengers have gotten to their destinations ***")
    return


def getOn(tripNum): # tripNum indicates if it's trip 1 or trip 2
    '''this prints who is getting on which bus'''
    waiting = Person.travelling[:]
    for bus in Bus.all:
        for person in waiting[:]:
            if bus.isFull():
                print("*** Bus",bus.getID(),"is full and cannot take on more passengers.")
            else:
                if person.locate() == bus.getRoute()[tripNum-1]\
                        and person.getDestination() in bus.getRoute()[tripNum:]:
                    print(person.getName(),"takes route", bus.getID(), "bus to",
                          bus.getRoute()[tripNum])
                    person.places.append(bus.getRoute()[tripNum]) # updating person.places list
                    bus.curCap += 1 # update bus passenger count
                    waiting.remove(person)
                    # so that people who have taken trip 1 or trip 2 will not get looped for the second time
                    if person.locate() == person.getDestination():
                        print("***", person.getName(), "has arrived at the final destination:",
                              person.getDestination())
                        Person.arrived.append(person)
                        Person.travelling.remove(person) #
    print("\n")
    for person in waiting:
        print(person.getName(),"is currently waiting for another bus in",person.getOrigin())
    return


def getOff():
    '''this clears the passenger count of the bus when everyone gets off'''
    for bus in Bus.all:
        bus.curCap = 0


def locateBus(n):
    '''this prints the current location of the bus'''
    for bus in Bus.all:
        if n == 0:
            print("Bus",bus.getID(),"is in",bus.getRoute()[0])
        else:
            print("Bus",bus.getID(),"is now in",bus.locate())


def drive(n):  # n indicates if it's trip 1 or trip 2
    '''this prints current status and updates current location of each bus:
    where it's driving from, where it's driving to, how many passengers on board'''
    for bus in Bus.all:
        print("Bus",bus.getID(),"drives from",bus.getRoute()[n-1],"to",bus.getRoute()[n]\
              +" >>> Number of passenger on board:",bus.passengerCount())
        bus.curLoc = bus.getRoute()[n]



print(">>> System check...\n")

check_bus()

print(" ")
print(" ")



print(">>> At the beginning...\n")

pplInTown() # prints who's in which town

print(" ")
print(" ")

locateBus(0)

print(" ")
print(" ")

print(">>> Starting the 1st trip...\n")

getOn(1) # passengers choose the bus for trip 1

print(" ")
print(" ")

drive(1) # shows bus location and bus status, e.g. how many people on board

print(" ")
print(" ")


print(">>> End of the first trip...\n")

getOff() # all passengers get off and bus' current capacity count is cleared
pplInTown()

print(" ")
print(" ")

locateBus(1) # prints current location of each bus

print(" ")
print(" ")

print(">>> Starting the 2nd trip...\n")

getOn(2) # passengers choose the bus for trip 2

print(" ")
print(" ")

drive(2) # shows bus location and bus status, e.g. how many people on board
print(" ")
print(" ")

print(">>> End of the 2nd trip...\n")

getOff() # all passengers get off and bus' current capacity count is cleared
pplInTown() # prints who's in which town

print(" ")
print(" ")

locateBus(2) # prints current location of each bus
