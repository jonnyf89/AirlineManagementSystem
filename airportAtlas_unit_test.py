'''Unit tests for the AirportAtlas class'''
import unittest
from airportAtlas import AirportAtlas 


class AtlasTest(unittest.TestCase):

    def setUp(self):
        print ("Before the Test")

        self.known_values = (("DUB", "SYD", 17215.275673402804), ("DUB", "AAL", 1096.7379627823607), ("DUB","CDG", 784.9716519536988))
        #note: known values were rounded to nearest km, I ran the test and the values that my function produced
        #were the same, only not rounded, so I added the decimal values to the test
        self.atlas1 = AirportAtlas("airport.csv")                                   #creates AirportAtlas object        

        
    def test_getDistBetween_known_values(self):                                     #tests the get_distance_between_airports method
        for code_1, code_2, dist in self.known_values:
            
            result = self.atlas1.get_distance_between_airports(code_1, code_2)

            self.assertEqual(dist, result)

    def test_distance_between_dublin_is_zero(self):                                 #tests the get_distance_between_airports method
        code_1 = 'DUB'
        code_2 = 'DUB'
        dist = 0
        result = self.atlas1.get_distance_between_airports(code_1, code_2)
        self.assertEqual(dist, result)

    def test_getCountry(self):                                                      #tests getCountry method
        getCountryOutput = self.atlas1.getCountry('DUB')
        self.assertEqual(getCountryOutput, "Ireland") 
        getCountryOutput = self.atlas1.getCountry('SYD')
        self.assertEqual(getCountryOutput, "Australia")
        getCountryOutput = self.atlas1.getCountry('IUD')
        self.assertEqual(getCountryOutput, "Qatar") 

    

    def tearDown(self):
        print ("After the Test")

if __name__ == '__main__':
    unittest.main()
