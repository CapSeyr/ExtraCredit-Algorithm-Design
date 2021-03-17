import sys

#########################################
#           verifyValues()              #
# Ensures all items in user file can be #
# changed into numeric values           #
#########################################
def verifyValues(values):
    for item in values:
        #testValue = item
        try:
            float(item)
        except ValueError:
            print("Please ensure values in file are only numeric values and re-run program.")
            print("File contains item \"" + item + "\" which is non numeric")
            sys.exit()
        else: 
            continue
    return        


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

################################################## 
#            findTowerLocations()                #
# This function calls the remove houses function #
# and keeps track of the house list to exit when #
# there are no more houses.                      #
##################################################

def findTowerLocations(houses, towers):
    while len(houses) > 0:
        removeHouses(houses, towers)
    return
        
##################################
#       removeHouses()           #
# removes houses that are within #
# a 4 mile radius of the most    #
# recently placed base station   #
##################################
def removeHouses(houses, towers):
    towers.append(houses[0] + 4) 
    towerLocation = houses[0] + 4
    while len(houses) > 0:
        if houses[0] >= towerLocation -4 and houses[0] <= towerLocation +4:
            houses.pop(0)
        else:
            return

#####################################
#       writeTowerLocations()       #
# prints tower locations to file    #
#####################################
def writeTowerLocations(towers):
    with open("StationLocations.txt", "a") as appendFile:
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

verifyValues(houseDistances)

houseDistances = [float(x) for x in houseDistances] #make the house locations list ordered from closest to furthest.
houseDistances.sort()           


towerFile = open("StationLocations.txt", "w+")        #create or open file
towerFile.write("Base Station Locations\n")                #write to output file
towerFile.close()                                   #close output file.

towerLocations = []

findTowerLocations(houseDistances, towerLocations)

writeTowerLocations(towerLocations)
print("View your tower placements in the StationLocations.txt file!")
