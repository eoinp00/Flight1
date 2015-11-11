class Tower:
    aFlightList = []


    def __init__(self, towerName, aFlightList):
        self.towerName = towerName
        self.aFlightList = aFlightList

    # def requestFlightClearance(self, anAirplane,):
    #     for anAirplane.planeType in self.aFlightList:


    # def validateFlightNum(self):
    #     for i in self.aFlightList:
    #         if self.aFlightList[:2].isalpha() and self.aFlightList[2:]:
    #             return True
    #         else:
    #             print ("Sorry, invalid flight number")
    #             self.aFlightList.remove([i])

    # def validateFlightNum(self):
    #     for i in range(0, len(self.aFlightList)):
    #         aFlightListAlpha = self.aFlightList[i]
    #         aFlightListNum = self.aFlightList[i]
    #         if aFlightListAlpha[:2].isalpha() and aFlightListNum[2:].isnumeric():
    #             print ("BOTH ARE VALID")
    #             #return True
    #         else:
    #             print ("Sorry, invalid flight number")
    #             self.aFlightList.remove(i)
    #             #self.aFlightList.pop(i)
    #
    def validateFlightNum(self):
        ##Checks the towers "morning" flight list and removes invalid items.
        self.validFlightList = []
        self.invalidFlightList = []
        for i in range(0, len(self.aFlightList)):

            aFlightListAlpha = self.aFlightList[i]
            aFlightListNum = self.aFlightList[i]
            if not aFlightListAlpha[:2].isalpha() or not aFlightListNum[2:].isnumeric():
                print ("Sorry, invalid flight number", )
                self.invalidFlightList.append(self.aFlightList[i])
            else:
                print ("Both Valid")
                self.validFlightList.append(self.aFlightList[i].upper())
            print (self.validFlightList, self.invalidFlightList)
                #self.aFlightList.remove(i)
                #self.aFlightList.pop(i)

    def updateFlightList(self, aFlightList, validateFlightNum):
        if validateFlightNum == True:
            self.aFlightList.append(validateFlightNum)   ##.self at start means instanciated "dublin tower" will have this modified list as an attribute (instead of the list being cleared each time method ends)

