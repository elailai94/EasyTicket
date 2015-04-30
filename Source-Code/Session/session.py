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

    'Fields: network, origin station, destination station, journey fare'

    # Initializes the object.
    def __init__(self, arg):
        self.__network = arg
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
            journey_fare = 4.80
            self.__journey_fare = journey_fare
    	    return journey_fare
    

    # Increases the amt of fare paid field by amount.
    def pay_journey_fare(self, amount):
    	isinstance(self, Session)
    	self.__amt_of_fare_paid += amount


    # Returns True if the journey fare has been paid in full. Otherwise,
    # False is return.
    def is_journey_fare_paid(self):
    	isinstance(self, Session)
    	return self.__amt_of_fare_paid >= self.__journey_fare

    #
    def print_ticket(self):
        isinstance(self, Session)
        print 'London Underground'
        print time.strftime('%d %b %y')


    def return_change(self):
        isinstance(self, Session)
        return self.__amt_of_fare_paid - self.__journey_fare
