'''class for country object'''
class Country:
    def __init__(self, name, currency_name):                    #constructor
        self.name = name
        self.currency_name = currency_name

    def __str__(self):
        return "%s %s" %(self.name, self.currency_name)
