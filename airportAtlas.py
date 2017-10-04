'''Airport atlas class holds information about instances of airport class'''
'''it takes a csv file as an input and uses this to populate a dictionary object with relevant data about each airport'''

import csv
import math
from airport import Airport

class AirportAtlas:
    __airportDict = {}                              #this is the dictionary object that we will populate with airport data
    
    def __init__(self, csvFile):                    #the constructor method has the loadData method as an attribute 
        self.loadData(csvFile)

    def loadData(self, fileName):                               #the loadData method loads the dictionary object with aircraft data. It does not need to be called  
        try:                                                    #as it is invoked automatically by the constructor.
            with open(fileName, errors = 'ignore') as csvfile:      #I use 'errors = 'ignore'' here because it is more effective than a try catch
                reader = csv.DictReader(csvfile)                    #Please see note 1 in supporting document
                for row in reader:
                    self.__airportDict[row['Code']]= Airport(row['AirportID'], row['AirportName'], row['Country'], row['CityName'], row['Lat'], row['Long'])
        except FileNotFoundError:
            print("No CSV file found.")

    def getAirport(self, code):             #takes an airport code as input and returns airport information
        return self.__airportDict[code]

    def getCountry(self, code):             #takes an airport code as input and returns airport country
        try:                                #this try catch ensures the programme does not crash in response to an unknown airport code being inputted
            airport1 = self.getAirport(code)
            return airport1.country
        except Exception:
            return "Unable to get airport information"


    def distance_on_unit_sphere(self, lat1, long1, lat2, long2):            #calculates and returns the distance between 2 points with given lat and long
        radian_degrees = (math.pi*2)/360
        
        phi1 = (90-lat1) * radian_degrees
        phi2 = (90-lat2) * radian_degrees

        theta1 = long1 * radian_degrees
        theta2 = long2 * radian_degrees

        x = math.sin(phi1)* math.sin(phi2) * math.cos(theta1 - theta2) + math.cos(phi1) * math.cos(phi2)
        y = math.acos(x)
        distance = y * 6371

        return distance

    def get_distance_between_airports(self, code1, code2):          #uses the distance_on_unit_sphere method to calculate the distance between 2 airports
        try:
            airport1 = self.getAirport(code1)
            airport2 = self.getAirport(code2)
            return self.distance_on_unit_sphere(airport1.lat, airport1.long, airport2.lat, airport2.long)
        except Exception:
            return -1

