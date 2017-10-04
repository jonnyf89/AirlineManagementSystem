'''Unit tests for the Journey class'''
import unittest
from journey import Journey
from airportAtlas import AirportAtlas
from countryAtlas import CountryAtlas
from currencyAtlas import CurrencyAtlas
import sys
from io import TextIOWrapper, BytesIO


class JourneyTest(unittest.TestCase):
    def setUp(self):                                                #creates test variables for each test
        print ("Before the Test")

        self.airportAtlas1 = AirportAtlas("airport.csv")
        self.countryAtlas1 = CountryAtlas("countrycurrency.csv")
        self.currencyAtlas1 = CurrencyAtlas("currencyrates.csv")
        self.testDict = {'a:3', 'b:6', 'c:2'}


        '''journey objects for testing findCheapestFuel'''

        self.journey8 = Journey('JFK', ['SYD', 'NYC', 'DUB', 'GWY'], self.airportAtlas1, self.countryAtlas1, self.currencyAtlas1, 4000)
        self.journey8_expected_cheapest = ['SYD']

        self.journey9 = Journey('AOC', ['CNG', 'OXD', 'GLO', 'PBV'], self.airportAtlas1, self.countryAtlas1, self.currencyAtlas1, 4000)
        self.journey9_expected_cheapest = ['PBV', 'OXD']

        self.journey10 = Journey('ACC', ['LCY', 'LWK', 'MTJ'], self.airportAtlas1, self.countryAtlas1, self.currencyAtlas1, 4000)
        self.journey10_expected_cheapest = ['ACC']



        '''Required tests for determine_jump_order:'''
        '''Test1 : 4 destinations, aircraft has sufficient range'''
        self.craftRange = 4000
        self.home = 'DUB'
        self.destList = ['FRA','LGW','MUC', 'LGG']
        self.journey1 = Journey(self.home, self.destList, self.airportAtlas1, self.countryAtlas1, self.currencyAtlas1, self.craftRange)
        self.expected_output_journey1_DJO = ("The most efficient route is as follows:\n"
                                                "DUB  to  LGW\n"
                                                "LGW  to  LGG\n"
                                                "LGG  to  FRA\n"
                                                "Final hop is from  FRA  to  MUC\n"
                                                "Including return trip from MUC to DUB, total journey distance is 2795.26km\n")

        '''Test2 : 3 destinations, aircraft has sufficient range'''
        self.craftRange2 = 8000
        self.home2 = 'DUB'
        self.destList2 = ['NOC', 'KIR', 'ORK']
        self.journey2 = Journey(self.home2, self.destList2, self.airportAtlas1, self.countryAtlas1, self.currencyAtlas1, self.craftRange2)
        self.expected_output_journey2_DJO = ("The most efficient route is as follows:\n"
                                                "DUB  to  NOC\n"
                                                "NOC  to  KIR\n"
                                                "Final hop is from  KIR  to  ORK\n"
                                                "Including return trip from ORK to DUB, total journey distance is 685.52km\n")

        '''Test3 : 2 destinations, aircraft has sufficient range'''
        self.craftRange3 = 8000
        self.home3 = 'JFK'
        self.destList3 = ['NYC', 'LGA']
        self.journey3 = Journey(self.home3, self.destList3, self.airportAtlas1, self.countryAtlas1, self.currencyAtlas1, self.craftRange3)
        self.expected_output_journey3_DJO = ("The most efficient route is as follows:\n"
                                                "JFK  to  LGA\n"
                                                "Final hop is from  LGA  to  NYC\n"
                                                "Including return trip from NYC to JFK, total journey distance is 51.29km\n")

        '''Test4 : not enough destinations entered'''
        self.craftRange4 = 4000000
        self.home4 = 'JFK'
        self.destList4 = ['NYC']
        self.journey4 = Journey(self.home4, self.destList4, self.airportAtlas1, self.countryAtlas1, self.currencyAtlas1, self.craftRange4)
        #expected result: SystemExit

        '''Test5 : aircraft range insufficient to reach one of the destinations'''
        self.craftRange5 = 200
        self.home5 = 'DUB'
        self.destList5 = ['ORK', 'JFK', 'NYC']
        self.journey5 = Journey(self.home5, self.destList5, self.airportAtlas1, self.countryAtlas1, self.currencyAtlas1, self.craftRange5)
        #expected result: SystemExit

        '''Test6 : aircraft range insufficient to make the return trip'''
        self.craftRange6 = 2595
        self.home6 = 'BHX'
        self.destList6 = ['LUX', 'PRG', 'BUD', 'BUS']
        self.journey6 = Journey(self.home6, self.destList6, self.airportAtlas1, self.countryAtlas1, self.currencyAtlas1, self.craftRange6)
        #expected result: SystemExit




    def test_getRange(self):
        self.assertEqual(self.journey1.getRange(), 4000)                        #determines if self.journey1.getRange() returns 4000
        self.assertEqual(self.journey5.getRange(), 200)
        self.assertEqual(self.journey3.getRange(), 8000)


    def test_getStops(self):
        self.assertEqual(self.journey1.getStops(), (self.journey1.home, self.journey1.destList))        #determines if self.journey1.getStops returns:
        self.assertEqual(self.journey6.getStops(), (self.journey6.home, self.journey6.destList))        # 'DUB', ['FRA','LGW','MUC', 'LGG']
        self.assertEqual(self.journey10.getStops(), (self.journey10.home, self.journey10.destList))
         

    def test_findCheapestFuel(self):
        self.assertCountEqual(self.journey8.findCheapestFuel(), self.journey8_expected_cheapest)#assertCountEquals checks that the dictionaries contain the same items
        self.assertCountEqual(self.journey9.findCheapestFuel(), self.journey9_expected_cheapest) #the benefit is that they do not need to be in the same order/sequence
        self.assertCountEqual(self.journey10.findCheapestFuel(), self.journey10_expected_cheapest)

    def test_checkRefuels(self):
        self.assertEqual(self.journey2.checkRefuels(), 0)
        
    
        '''The below function, determine_jump_order, does not return a value, rather it prints lines when invoked. This means that I could not unit test it
        the traditional way. The solution I used was to redirect stdout to a byte array, and use assertEqual to verify that the byte array matches the
        expected output.'''
    def test_determine_jump_order(self):

        '''Test 1'''
        # setup the environment
        old_stdout = sys.stdout                                                     #stores the current state of stdout, for restore later
        sys.stdout = TextIOWrapper(BytesIO(), sys.stdout.encoding)                  #redirects stdout
        
        self.journey1.determine_jump_order()                                        #executes determine_jump_order

        # get output
        sys.stdout.seek(0)                                                          # jump to the start
        out = sys.stdout.read()                                                     # assigns the current contents of the stdout buffer to a variable
        self.assertEqual(out, self.expected_output_journey1_DJO)            # asserts if the variable out(assigned above) equals the expected print output

        
        # restore stdout
        sys.stdout.close()
        sys.stdout = old_stdout
        

        '''Test2'''
         # setup the environment
        old_stdout = sys.stdout                                                     #stores the current state of stdout, for restore later
        sys.stdout = TextIOWrapper(BytesIO(), sys.stdout.encoding)                  #redirects stdout
        
        self.journey2.determine_jump_order()                                        #executes determine_jump_order

        # get output
        sys.stdout.seek(0)                                                          # jump to the start
        out = sys.stdout.read()                                                     # assigns the current contents of the stdout buffer to a variable
        self.assertEqual(out, self.expected_output_journey2_DJO)            # asserts if the variable out(assigned above) equals the expected print output

        
         # restore stdout
        sys.stdout.close()
        sys.stdout = old_stdout


        '''Test 3'''
        # setup the environment
        old_stdout = sys.stdout                                                     #stores the current state of stdout, for restore later
        sys.stdout = TextIOWrapper(BytesIO(), sys.stdout.encoding)                  #redirects stdout
        
        self.journey3.determine_jump_order()                                        #executes determine_jump_order

        # get output
        sys.stdout.seek(0)                                                          # jump to the start
        out = sys.stdout.read()                                                     # assigns the current contents of the stdout buffer to a variable
        self.assertEqual(out, self.expected_output_journey3_DJO)            # asserts if the variable out(assigned above) equals the expected print output

        
         # restore stdout
        sys.stdout.close()
        sys.stdout = old_stdout



        '''Test 4'''
        # setup the environment, In this instance we only redirect stdout to avoid printing outputs on the console
        old_stdout = sys.stdout                                                     #stores the current state of stdout, for restore later
        sys.stdout = TextIOWrapper(BytesIO(), sys.stdout.encoding)                  #redirects stdout

        with self.assertRaises(SystemExit):
            self.journey4.determine_jump_order()        
        
        # restore stdout
        sys.stdout.close()
        sys.stdout = old_stdout


        
        '''Test 5'''
        # setup the environment, In this instance we only redirect stdout to avoid printing outputs on the console
        old_stdout = sys.stdout                                                     #stores the current state of stdout, for restore later
        sys.stdout = TextIOWrapper(BytesIO(), sys.stdout.encoding)                  #redirects stdout

        with self.assertRaises(SystemExit):
            self.journey5.determine_jump_order()        
        
        # restore stdout
        sys.stdout.close()
        sys.stdout = old_stdout



        '''Test 6'''
        # setup the environment, In this instance we only redirect stdout to avoid printing outputs on the console
        old_stdout = sys.stdout                                                     #stores the current state of stdout, for restore later
        sys.stdout = TextIOWrapper(BytesIO(), sys.stdout.encoding)                  #redirects stdout

        with self.assertRaises(SystemExit):
            self.journey6.determine_jump_order()        
        
        # restore stdout
        sys.stdout.close()
        sys.stdout = old_stdout

    
    
    def tearDown(self):
        print ("After the Test")

if __name__ == '__main__':
    unittest.main()
