'''CountryAltlas class holds information on aircrafts'''
'''it takes a csv file as an input and uses this to populate a dictionary object with relevant data about each aircraft type'''
import csv
from country import Country

class CountryAtlas:
    __countryDict = {}                              #this is the dictionary object that we will populate with country data

    def __init__(self, csvFile):
        self.loadData(csvFile)                      #the constructor method has the loadData method as an attribute

    def loadData(self, fileName):                   #the loadData method loads the dictionary object with aircraft data. It does not need to be called
        try:                                        #as it is invoked automatically by the constructor.
            with open(fileName, errors = 'ignore') as csvfile:          #I use 'errors = 'ignore'' here because it is more effective than a try catch
                reader = csv.DictReader(csvfile)                        #Please see note 1 in supporting document
                for row in reader:
                    self.__countryDict[row['name']] = Country(row['currency_name'], row['currency_alphabetic_code'])
        except FileNotFoundError:
            print("No CSV file found.")

    def getCountry(self, name):                         #this method returns the dictionary entry associated with the provided country name
        return self.__countryDict[name]

    def showAll(self):                                  #this method show the entire contents of the countryDict
        return self.__countryDict
        
    def getCurrency(self, name):                        #this method returns the currency name associated with the provided country name
        country1 = self.getCountry(name)
        return country1.currency_name
