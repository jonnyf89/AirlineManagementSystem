import unittest
from countryAtlas import CountryAtlas

class CountryAtlas_test(unittest.TestCase):
    def setUp(self):
        print ("Before the Test")

        self.atlas1 = CountryAtlas("countrycurrency.csv")                       #creating a series of test variables to test my methods

        self.afghanistan = "%s" % self.atlas1.getCountry('Afghanistan')
        self.thailand = "%s" % self.atlas1.getCountry('Thailand')
        self.ireland = "%s" % self.atlas1.getCountry('Ireland')

        self.italyCurrency = self.atlas1.getCurrency('Italy')
        self.southKoreaCurrency = self.atlas1.getCurrency('South Korea')
        self.kenyaCurrency = self.atlas1.getCurrency('Kenya')

    
    def test_getCountry(self):
        self.assertEqual(self.afghanistan, "Afghani AFN")       #determines if the output of self.atlas1getCoutry('Afghanistan') is 'Afghani AFN
        self.assertEqual(self.thailand, "Baht THB")
        self.assertEqual(self.ireland, "Euro EUR")

    def getCurrency(self):
        self.assertEqual(self.italyCurrency, "Euro")            #determines if the output of self.atlas1.getCurrency('Italy') is 'Euro'
        self.assertEqual(self.southKoreaCurrency,"Won")
        self.assertEqual(self.kenyaCurrency, "Kenyan Shilling")
            

    def tearDown(self):
        print ("After the Test")

if __name__ == '__main__':
    unittest.main()

