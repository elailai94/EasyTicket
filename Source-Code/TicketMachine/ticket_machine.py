#==============================================================================
# EasyTicket
#
# @description: Module for providing methods to work with TicketMachine objects
# @author: Elisha Lai
# @version: 1.4 30/04/2015
#==============================================================================

# Ticket machine module (ticket_machine.py)

from network import Network
from session import Session

# Object definition
class TicketMachine(object):
	

    'Fields: network, amt_of_money_collected, num_of_tickets_issued, current_session'
    # A TicketMachine is an object in which:
    # - network is a Network (network)
    # - amt_of_money_collected is a Float (amount of money collected on
    #   this ticket machine)
    # - num_of_tickets_issued is an Int (number of tickets issued on
    #   this ticket machine)
    # - current_session is a Session (current session in progress on
    #   this ticket machine)


    # Instantiates the object. 
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'self'):
    	    cls.self = object.__new__(cls)
    	return cls.self


    # Returns a string representation of the object.
    def __repr__(self):
        return 'Amount of Money Collected:%.2f  Number of Tickets Issued:%d\nCurrent Session:%r' \
               % (self.__amt_of_money_collected, self.__num_of_tickets_issued, self.__current_session) 


    # Initializes the object.
    def __init__(self):
    	self.__network = Network()
    	self.__network.build_network()
    	self.__amt_of_money_collected = 0.0
    	self.__num_of_tickets_issued = 0
    	self.__current_session = None

    # Initiates a new session.
    def start_session(self):
    	isinstance(self, TicketMachine)
        self.__current_session = Session(self.__network)


    # Sets the origin station for the current session (if any).
    def set_origin_station(self, station):
        isinstance(self, TicketMachine)
        if self.__current_session != None:
            current_session = self.__current_session
            current_session.set_origin_station(station)


    # Sets the destination station for the current session (if any).
    def set_destination_station(self, station):
    	isinstance(self, TicketMachine)
    	if self.__current_session != None:
    		self.__current_session.set_destination_station(station)


    # Calculates the journey fare for the current session (if any).
    def calculate_journey_fare(self):
    	isinstance(self, TicketMachine)
        if self.__current_session != None:
        	return self.__current_session.calculate_journey_fare()


    # Pays for the journey fare for the current session (if any).
    def pay_journey_fare(self, amount):
    	isinstance(self, TicketMachine)
    	if self.__current_session != None:
    		self.__current_session.pay_journey_fare(float(amount))


    # Returns True if the journey fare for the current session (if any)
    # has been paid in full. Otherwise, False is return.
    def is_journey_fare_paid(self):
        isinstance(self, TicketMachine)
        if self.__current_session != None:
            return self.__current_session.is_journey_fare_paid()

    # Prints the ticket for the current session (if any).
    def print_ticket(self):
    	isinstance(self, TicketMachine)
    	if self.__current_session != None:
    		self.__current_session.print_ticket()


    # Returns change for the current session (if any).
    def return_change(self):
        isinstance(self, TicketMachine)
        if self.__current_session != None:
            return self.__current_session.return_change()


    # Ends the current session.
    def end_session(self):
    	isinstance(self, TicketMachine)
    	self.__num_of_tickets_issued += 1
    	self.__current_session = None
