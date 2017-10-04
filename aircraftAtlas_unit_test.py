'''Unit test for the AircraftAtlas class'''
import unittest
from aircraftAtlas import AircraftAtlas

atlas1 = AircraftAtlas("aircraft.csv")              #creates AircraftAtlas object
a747output = "%s" % atlas1.getAircraft('747')       #4 tests for the getAircraft method
aV22output = "%s" % atlas1.getAircraft('V22')
anA330output = "%s" % atlas1.getAircraft('A330')
anF50output = "%s" % atlas1.getAircraft('F50')

class AircraftAtlasTest(unittest.TestCase):
    def setUp(self):
        print ("Before the Test")
        self.atlas1 = AircraftAtlas("aircraft.csv")              #creates AircraftAtlas object
        self.a747output = "%s" % self.atlas1.getAircraft('747')       #4 tests for the getAircraft method
        self.aV22output = "%s" % self.atlas1.getAircraft('V22')
        self.anA330output = "%s" % self.atlas1.getAircraft('A330')
        self.anF50output = "%s" % self.atlas1.getAircraft('F50')
        
    def test_getAircraft(self):
        
        self.assertEqual(self.a747output, "jet imperial Boeing 15680") #range in km is calculated as by range in miles*1.6, rounded to 0 decimal points
        self.assertEqual(self.aV22output, "turboprop imperial Boeing 2595")
        self.assertEqual(self.anA330output, "jet metric Airbus 13430")
        self.assertEqual(self.anF50output, "turboprop metric Fokker 2055")

    def tearDown(self):
        print ("After the Test")

if __name__ == '__main__':
    unittest.main()
