'''unit test class for my aircraft class'''
import unittest
from aircraft import Aircraft


class AircraftTestCase(unittest.TestCase):

    def setUp(self):
        print ("Before the Test")

        self.aircraft1 = Aircraft('type', 'metric', 'manufacturer', 2000) #usually aircraft objects are populated from the csv file using the aircraftAtlas class
        self.aircraft2 = Aircraft('type', 'imperial', 'manufacturer', 1500)    # for the purpose of this test I have selected these values
        self.aircraft3 = Aircraft('type', 'metric', 'manufacturer', 8000)

    def test_getRange(self):
        self.assertEqual(self.aircraft1.getRange(), 2000)
        self.assertEqual(self.aircraft2.getRange(), 2400) #aircraft 2 uses imperial units, so we multiply range by 1.6 to find km value 
        self.assertEqual(self.aircraft3.getRange(), 8000)

    def tearDown(self):
        print ("After the Test")

if __name__ == '__main__':
    unittest.main()
