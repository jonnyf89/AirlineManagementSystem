'''Airport class holds attributes of the airport object'''
class Airport:
    
    def __init__(self, id, name, country, city, lat, long):             #constructor
        
        self.id = int(id)
        self.name = name
        self.country = country
        self.city = city
        self.lat = float(lat)
        self.long = float(long)

    def __str__(self):
        return "%d %s %s %s %f %f" % (self.id, self.name,self.country,
                                      self.city,self.lat,self.long)



