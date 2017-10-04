import unittest
from currencyAtlas import CurrencyAtlas

class CurrencyAtlas_test(unittest.TestCase):

    def setUp(self):                                                #creates test variables
        print ("Before the Test")

        self.atlas1 = CurrencyAtlas("currencyrates.csv")

        self.barbados_dollar = "%s" % self.atlas1.getCurrency('BBD')
        self.mexican_peso = "%s" % self.atlas1.getCurrency('MXN')
        self.french_franc = "%s" % self.atlas1.getCurrency('FRF')

        self.polish_zloty_exch = self.atlas1.getExch('PLN')
        self.columbian_peso_exch = self.atlas1.getExch('COP')
        self.canadian_dollar_exch = self.atlas1.getExch('CAD') 

    def test_getCurrency(self):
        self.assertEqual(self.barbados_dollar, "0.474424 Barbados Dollar")#determines if output self.atlas1.getCurrency('BBD') is "0.474424 Barbados Dollar"
        self.assertEqual(self.mexican_peso, "0.061380 Mexican Peso") #expected output for exchange rate expressed with 6 decimal points
        self.assertEqual(self.french_franc, "0.152400 French Franc")

    def test_getExch(self):
        self.assertEqual(self.polish_zloty_exch, 0.2417)                    #determines if output self.atlas.getExch('PLN') is 0.2417
        self.assertEqual(self.columbian_peso_exch, 0.0003621)
        self.assertEqual(self.canadian_dollar_exch, 0.7423)

    def tearDown(self):
        print ("After the Test")

if __name__ == '__main__':
    unittest.main()
