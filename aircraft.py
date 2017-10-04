'''A class for the aircraft object'''
class Aircraft:
    
    def __init__(self, craftType, units, manufacturer, craftRange): #constructor method
        self.craftType = craftType
        self.units = units
        self.manufacturer = manufacturer
        self.floatCraftRange = float(craftRange)
        if self.units == 'metric':                                  #since some airports have their range in miles and some in km, this if statement 
            self.floatCraftRange = float(self.floatCraftRange)      #converts miles to km, so that range values are consistent across all aircraft objects
        elif self.units == 'imperial':
            self.floatCraftRange = float(self.floatCraftRange*1.6)
        else:
            self.floatCraftRange = float(0.0)
        self.craftRange = int(self.floatCraftRange)
        
    def __str__(self):
        return "%s %s %s %d" % (self.craftType, self.units,
                                     self.manufacturer, self.craftRange)

    def getRange(self):                                         #method which returns the range of an aircraft object
        try:
            return self.craftRange
        except Exception:
            return ("getRange failed")
