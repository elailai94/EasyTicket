#==============================================================================
# EasyTicket
#
# @description: Module for providing methods to work with TicketMachine objects
# @author: Elisha Lai
# @version: 1.1 26/04/2015
#==============================================================================

# Ticket machine module (ticket_machine.py)

from network import Network
from session import Session

# Object definition
class TicketMachine(object):
	
    'Fields: network, amt_of_money_collected, num_of_tickets_issued, current_session'


    # Instantiates the object. 
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'self'):
    	    cls.self = object.__new__(cls)
    	return cls.self


    # Initializes the object.
    def __init__(self):
    	self.__network = Network()
    	self.__network.build_network()
    	self.__amt_of_money_collected = 0.0
    	self.__num_of_tickets_issued = 0
    	self.__current_session = None

    # Initiates a new session.
    def new_session(self):
    	isinstance(self, TicketMachine)
        self.__current_session = Session(self.__network)
