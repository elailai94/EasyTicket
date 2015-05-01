#==============================================================================
# EasyTicket
#
# @description: Module for providing methods to work with Session objects
# @author: Elisha Lai
# @version: 1.5 30/04/2015
#==============================================================================

# Session module (session.py)

import time

# Object definition
class Session:


    'Fields: network, journey_fares, origin_station, destination_station, journey_fare, amt_of_fare_paid'
    # A Session is an object in which:
    # - network is a Network (network)
    # - journey_fares is a JourneyFares (journey fares)
    # - origin_station is a Str (origin station)
    # - destination_station is a Str (destination station)
    # - journey_fare is a Float (journey fare from origin station to
    #   destination station)
    # - amt_of_fare_paid is a Float (amount of fare paid so far)


    # Initializes the object.
    def __init__(self, network, journey_fares):
        self.__network = network
        self.__journey_fares = journey_fares
        self.__origin_station = None
        self.__destination_station = None
        self.__journey_fare = 0.0
        self.__amt_of_fare_paid = 0.0


    # Returns a string representation of the object.
    def __repr__(self):
        return 'Origin Station:%s  Destination Station:%s  Journey Fare:%.2f  Amount of Fare Paid:%.2f' \
               % (self.__origin_station, self.__destination_station, \
               self.__journey_fare, self.__amt_of_fare_paid) 


    # Sets the origin station field to station.
    def set_origin_station(self, station):
	isinstance(self, Session)
	self.__origin_station = station


    # Sets the destination station field to station.
    def set_destination_station(self, station):
	isinstance(self, Session)
	self.__destination_station = station


    # Calculates the journey fare for traveling from origin station to
    # destination station.
    def calculate_journey_fare(self):
    	isinstance(self, Session)
    	if self.__origin_station != None and\
    	   self.__destination_station != None:
            shortest_path = self.__network.find_shortest_path(self.__origin_station, \
                            self.__destination_station)[1]
            zones_visited = self.__network.get_zones_visited(shortest_path)
            min_zone_visited = min(zones_visited)
            max_zone_visited = max(zones_visited)
            
            if min_zone_visited >= 5:
                journey_fare = self.__journey_fares.lookup_fare('Tier 1')
            elif min_zone_visited >= 4:
                if max_zone_visited <= 7:
                    journey_fare = self.__journey_fares.lookup_fare('Tier 1')
                else:
                    journey_fare = self.__journey_fares.lookup_fare('Tier 2')
            elif min_zone_visited >= 3:
                if max_zone_visited <= 5:
                    journey_fare = self.__journey_fares.lookup_fare('Tier 1')
                else:
                    journey_fare = self.__journey_fares.lookup_fare('Tier 2')
            if min_zone_visited >= 2:
                if max_zone_visited <= 4:
                    journey_fare = self.__journey_fares.lookup_fare('Tier 1')
                elif max_zone_visited <= 7:
                    journey_fare = self.__journey_fares.lookup_fare('Tier 2')
                else:
                    journey_fare = self.__journey_fares.lookup_fare('Tier 4')
            else:
                if max_zone_visited <= 3:
                    journey_fare = self.__journey_fares.lookup_fare('Tier 1')
                elif max_zone_visited <= 5:
                    journey_fare = self.__journey_fares.lookup_fare('Tier 2')
                elif max_zone_visited <= 6:
                    journey_fare = self.__journey_fares.lookup_fare('Tier 3')
                elif max_zone_visited <= 7:
                    journey_fare = self.__journey_fares.lookup_fare('Tier 5')
                else:
                    journey_fare = self.__journey_fares.lookup_fare('Tier 6')

            self.__journey_fare = journey_fare
            return journey_fare


    # Returns the journey fare field.
    def get_journey_fare(self):
        isinstance(self, Session)
        return self.__journey_fare
    

    # Increases the amt of fare paid field by amount.
    def pay_journey_fare(self, amount):
    	isinstance(self, Session)
    	self.__amt_of_fare_paid += amount


    # Returns the amount of fare paid.
    def refund_amount_of_fare_paid(self):
        isinstance(self, Session)
        amount_of_fare_paid = self.__amt_of_fare_paid
        self.__amt_of_fare_paid = 0.0
        return amount_of_fare_paid


    # Returns True if the journey fare has been paid in full. Otherwise,
    # False is return.
    def is_journey_fare_paid(self):
    	isinstance(self, Session)
    	return self.__amt_of_fare_paid >= self.__journey_fare


    # Returns the remaining amount of fare to be paid.
    def get_remaining_fare_to_be_paid(self):
        isinstance(self, Session)
        if not self.is_journey_fare_paid():
            return self.__journey_fare - self.__amt_of_fare_paid
        else:
            return 0.0


    # Prints the ticket for the journey.
    def print_ticket(self):
        isinstance(self, Session)
        journey_fare_str = u'\xA3' + '%.2f' % (self.__journey_fare)
        print '------------------------------------------'
        print '|        >> London Underground <<        |'
        print '| Single  ' + '%30s' % (journey_fare_str) + ' |'
        print '|                                        |'
        print '| ' + time.strftime('%d %b %y') + '%29s' % (self.__destination_station) + ' |'
        print '|     This side up >> Not for resale     |' 
        print '------------------------------------------'


    # Returns change. 
    def return_change(self):
        isinstance(self, Session)
        if self.is_journey_fare_paid():
            return self.__amt_of_fare_paid - self.__journey_fare
        else:
            return 0.0
