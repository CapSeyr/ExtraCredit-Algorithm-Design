

#########################################
#              intakeFile()             #
# intakes file and verifies that the    #
# file exists.                          #
#########################################
def intakeFile():
    while True:
        input_file = input("Please input house location/distances file name: ")
        try:
            return_file = open(input_file, "r")
        except OSError:
            print("Error accessing file, please try again: ")
        else:
            return return_file

def findTowerLocations(houses, towers):
    while len(houses) > 0:
        removeHouses(houses, towers)
    return
        

def removeHouses(houses, towers):
    towers.append(houses[0] + 4) 
    towerLocation = houses[0] + 4
    while len(houses) > 0:
        if houses[0] >= towerLocation -4 and houses[0] <= towerLocation +4:
            houses.pop(0)
        else:
            return

def writeTowerLocations(towers):
    with open("TowerLocations.txt", "a") as appendFile:
        i = 1
        for item in towers:
            appendFile.write("Base Station " + str(i) + ": mile %s\n" % item)
            i += 1
    return        

#def removeHouses


#################################
#      Main Block of Code       #
#################################

retrievedFile = intakeFile()     #intake user file
content = retrievedFile.read()   #read user file and store the contents

houseDistances = content.split() #split the conent into a list
retrievedFile.close()            #close the file

houseDistances = [float(x) for x in houseDistances] #make the house locations list ordered from closest to furthest.
houseDistances.sort()           
print(houseDistances)

towerFile = open("TowerLocations.txt", "w+")        #create or open file
towerFile.write("Base Station Locations\n")                #write to output file
towerFile.close()                                   #close output file.

towerLocations = []

findTowerLocations(houseDistances, towerLocations)

writeTowerLocations(towerLocations)
print("View your tower placements in the TowerLocations.txt file!")
