'''This is my which imports required classes, takes inputs from the users and runs the programme'''
from airportAtlas import AirportAtlas
from countryAtlas import CountryAtlas
from currencyAtlas import CurrencyAtlas
from aircraftAtlas import AircraftAtlas
from journey import Journey
import sys

def main():
    airportAtlas1 = AirportAtlas("airport.csv")                                 #creates atlases
    countryAtlas1 = CountryAtlas("countrycurrency.csv")
    currencyAtlas1 = CurrencyAtlas("currencyrates.csv")
    aircraftAtlas1 = AircraftAtlas("aircraft.csv")
    numberDestinations = 0
    craft = input("Please specify the code for the aircraft you will be using:") #aircraft input
    craft = craft.upper()                                                       #makes input uppercase, so inputs can be entered in uppercase or lowercase 
    try:
        craft = aircraftAtlas1.getAircraft(craft)                                           #error handling, running the inputs through getAircraft ensures
        craftRange = craft.getRange()                                                       #that they are valid codes
    except Exception:                                                                                                   
        print("Invalid aircraft code entered, please check it and try again")
        sys.exit(0)
    home = input("Please enter the starting airport code:")                                 #home airport input
    home = home.upper()                                                         #makes input uppercase, so inputs can be entered in uppercase or lowercase  
    try:
        airportAtlas1.getAirport(home)                                                      #checks for valid aircraft code
    except Exception:
        print("Invalid home airport code entered, please check it and try again.") 
        raise SystemExit
    portList = [home]
    destList = []
    port = ''

    for i in range(4):
        if port != '0':
            port = input("Please enter a destination airport(minimum 2), enter 0 when finished:")       #destination airports input
            port = port.upper()                                             #makes input uppercase, so inputs can be entered in uppercase or lowercase 
            if port != '0':
                portList.append(port)
                destList.append(port)
                try:
                    airportAtlas1.getAirport(port)
                except Exception:
                    print("Invalid airport code entered, please check it and try again.") 
                    raise SystemExit
    numberDestinations = len(destList)
    try:
        journey1 = Journey(home, destList, airportAtlas1, countryAtlas1, currencyAtlas1, craftRange)
    except Exception:
        print("Unable to create journey object")
    print("Range of aircraft is ", journey1.getRange(), "km", sep = '')

    try:
        journey1.determine_jump_order()
    except SystemExit:
        sys.exit(0)
    except Exception:
        if numberDestinations < 2:
            print("Not enough airports entered, minimum 3; home + 2 destintions.")
        else:
            print("Invalid airport code entered, cannot determine jump order.") 
            
    if journey1.fullTripPlusReturn != 0:
        print("You will need to refuel", journey1.checkRefuels(), "times.")

    if journey1.checkRefuels() > 0:
        print("Cheapest fuel can be bought at the following airports:", journey1.findCheapestFuel())            #tells user cheapest airport to buy fuel
        print("The costs of fuel in euro per litre at each of the selected airports are as follows:", journey1.airportExchDict)
        #above: tells user fuel prices at all inputted airports
main()
