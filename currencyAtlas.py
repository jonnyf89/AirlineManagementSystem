'''CurrencyAtlas class holds information on currencies'''
'''it takes a csv file as an input and uses this to populate a dictionary object with relevant data about each  currency'''

import csv
from currency import Currency

class CurrencyAtlas:
    __currencyDict = {}                             #this is the currency object that we will populate with aircraft data

    def __init__(self, csvFile):                    #the constructor method has the loadData method as an attribute 
        self.loadData(csvFile)

    def loadData(self, fileName):               #the loadData method loads the dictionary object with aircraft data. It does not need to be called
        try:                                    #as it is invoked automatically by the constructor.
            with open(fileName, errors  = 'ignore') as csvfile:     #I use 'errors = 'ignore'' here because it is more effective than a try catch 
                reader = csv.DictReader(csvfile)                    #Please see note 1 in supporting document
                for row in reader:
                    self.__currencyDict[row['code']] = Currency(row['exchangeRate'], row['name'])
        except FileNotFoundError:
            print("No CSV file found.")

    def getCurrency(self, code):                                #this method returns the dictionary entry associated with the provided code
        return self.__currencyDict[code]

    def showAll(self):                                          #returns the entire contents of the __currencyDict
        return self.__currencyDict

    def getExch(self, code):                                    #returns the exchange rate for a currency based on a given currnecy code.
        currency1 = self.getCurrency(code)
        return currency1.exchangeRate
