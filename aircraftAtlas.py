'''AircratAtlas class holds information on aircrafts'''
'''it takes a csv file as an input and uses this to populate a dictionary object with relevant data about each aircraft type'''
import csv
from aircraft import Aircraft
import sys

class AircraftAtlas:
    __aircraftDict = {}                                 #this is the dictionary object that we will populate with aircraft data

    def __init__(self, csvFileName):                    #the constructor method has the loadData method as an attribute
        self.loaddata(csvFileName)
        
    def loaddata(self, filename):                       #the loadData method loads the dictionary object with aircraft data. It does not need to be called
        try:                                            #as it is invoked automatically by the constructor.
            with open(filename, errors = 'ignore') as csvfile:          #I use 'errors = 'ignore'' here because it is more effective than a try catch 
                 reader = csv.DictReader(csvfile)                       #Please see note 1 in supporting document
                 for row in reader:
                     self.__aircraftDict[row['code']]= Aircraft(row['craftType'], row['units'], row['manufacturer'], row['craftRange'])
        except FileNotFoundError:
            print("No CSV file found")

    def getAircraft(self, code):                        #this method returns the dictionary entry associated with the provided code
        return self.__aircraftDict[code]
