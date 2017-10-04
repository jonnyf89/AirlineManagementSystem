'''The journey class figures out and returns all of the information that the user is requesting by using this programme'''
import sys
class Journey:
    def __init__(self, home, destList, airportAtlas, countryAtlas, currencyAtlas, craftRange): #the object requires a lot of inputs, including instances of
                                                                                                #atlas objects
        self.home = home
        self.destList = destList
        self.airportAtlas = airportAtlas
        self.countryAtlas = countryAtlas
        self.currencyAtlas = currencyAtlas
        self.portList = [home] + destList
        self.currencyAirportDict= {}
        self.currencyCountryDict= {}
        self.airportExchDict = {}
        self.countryList = []
        self.currencyList = []
        self.cheapestFuelList = []
        self.craftRange = craftRange
        self.fullTripPlusReturn = 0
        self.jump = ''

    def getStops(self):                                                      #returns the destination list
        return(self.home, self.destList)

    def getRange(self):                                                      #returns the range of the aircraft
        return(self.craftRange)

    def determine_jump_order(self):                             #determines the order that destinations should be visited, see supporting document for 
        airportList = []                                        #details analysis 
        distDict = {}
        dist = 0
        totalDist = 0
        finalDest = self.home
        permDestList = self.destList #as the programme removes entries from destList as it runs, I create this variable to keep a copy of the full list

        def find_distances():                                     #finds the distances between stops and saves them in a dictionary
            for i in range(len(self.destList)):
                dist = self.airportAtlas.get_distance_between_airports(self.home, self.destList[i])
                distDict.update({self.destList[i]:dist})

        def findSmallest(dict):                                         #finds the hop with the smallest distance
            min_value = min(dict.values())
            min_key = next(key for key, value in dict.items() if value == min_value)
            return(min_key)

        def findSmallestValue(dict):                                    #finds tha distance(value) that is smallest
            min_value = min(dict.values())
            return(min_value)

        print("The most efficient route is as follows:")
        while len(self.destList)>1:                                     #plans the route, each hop sends the aircraft to the closest airport
            find_distances()
            self.jump = findSmallest(distDict)
            jumpDist = findSmallestValue(distDict)
            if jumpDist > self.craftRange:  
                print("Your selected aircraft cannot make the trip of %.2f"% jumpDist, "km to ", self.jump, ", you will have to select a different aircraft or add more stops.", sep = '')
                raise SystemExit                                        
                
            print(self.home, " to ", self.jump)
            self.destList.remove(self.jump)
            distDict.pop(self.jump)
            self.home = self.jump
            totalDist += jumpDist
        lastHopDist = self.airportAtlas.get_distance_between_airports(self.jump, self.destList[0])
        if lastHopDist == -1:
            print("Not enough airports entered, minimum 3; home + 2 destintions.")
            raise SystemExit                                                
        returnTripDist = self.airportAtlas.get_distance_between_airports(self.destList[0], finalDest)
        self.fullTripPlusReturn = totalDist + lastHopDist + returnTripDist
        
        if lastHopDist > self.craftRange:
            print("Your selected aircraft cannot make the trip of %.2f"% lastHopDist, "km to ", self.destList[0], ", you will have to select a different aircraft or add more stops.", sep = '')
            raise SystemExit                                               
        else:
            print("Final hop is from ", self.jump, " to ", self.destList[0])
        if returnTripDist > self.craftRange:
            print("Return trip is too far for this aircraft, you will need to choose a different aircraft or make another stop along the way.")
            raise SystemExit                                                
        else:
            print("Including return trip from ", self.destList[0], " to ", finalDest, ", total journey distance is %.2f" % self.fullTripPlusReturn, "km", sep = '')
    
    def findCheapestFuel(self):                                         #method to find and return the destination with the cheapest fuel
        for i in range(len(self.portList)):
            country = self.airportAtlas.getCountry(self.portList[i])
            self.currencyAirportDict.update({self.portList[i]:country})
            self.countryList.append(country)


        for i in range(len(self.portList)):
            currency = self.countryAtlas.getCurrency(self.countryList[i])
            self.currencyCountryDict.update({self.countryList[i]:currency})
            self.currencyList.append(currency)

        for i in range(len(self.portList)):
            exch = self.currencyAtlas.getExch(self.currencyList[i])
            self.airportExchDict.update({self.portList[i]:exch})


        min_value = float("inf")
        for k, v in self.airportExchDict.items():
            if v == min_value:
                cheapestFuelList.append(k)
            if v < min_value:
                min_value = v
                cheapestFuelList = []
                cheapestFuelList.append(k)
    
        return cheapestFuelList

    def getCraft(self):                                                 #returns the aircraft being used for the journey
        return(self.craft)

    def checkRefuels(self):                                             #calculates and returns the number of times the aircraft will beed to be refueled
        numberOfRefuels = int(self.fullTripPlusReturn/self.craftRange)
        return numberOfRefuels 
