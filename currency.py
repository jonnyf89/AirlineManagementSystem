'''Class for creating currency object'''

class Currency:                                 #constructor
    def __init__(self, exchangeRate, name):
        self.exchangeRate = float(exchangeRate)
        self.name = name


    def __str__(self):
        return "%f %s" % (self.exchangeRate, self.name)
    

