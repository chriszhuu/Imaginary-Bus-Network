(Bus system 1 is what I had for the original deadline. Bus system 2 is pretty different from BS 1. They each have their merits.) 

Bus systems 1 and 2 are different implementations of the same general idea. All buses have three stops: origin, destination 1 and destination 2. The system starts by checking the validity of each bus route and see if they travel on roads or not. If all routes are approved, we start the 1st trip, where all buses travel from their origins to their first stops. Passengers get on, then get off the bus. Then the 2nd trip starts, where buses go from their first stops to their final stops. 

In BS 1, the bus system essentially “operates” through the main file, where functions determine what to print based on list operations. The origin and destination of each person and each bus are strings, not Town objects.The classes are mostly static, except for appending new location to each person’s list of places, and bumping up each bus’s current capacity by 1 when passenger destination matches bus destination. In each class there aren’t many methods for classes to interact with each other. There is no storage of Person objects in other classes. I’m really proud of the display of information in this version.  

In BS 2, objects are created by reading from a file. Inputed string attributes are then processed and converted into objects. Town objects are now the attribute of Person objects and Bus objects, and each class has more methods. There is more class interaction in the methods, such as the getOn and getOff method in Person, and the drive method in Bus. The towns and buses store Person objects, which gets updated every time a person gets on or gets off a bus. The main file is mostly calling different class methods. 

## significant update: the BS 2 program now can write to and read from a backup file to reflect the current state of the system. It took a lot of work because when the program reads from backup files, there’re much more relevant attributes than before to be processed, and I had to modify class attributes to create updated objects from backup file.



