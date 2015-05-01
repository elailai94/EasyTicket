#==============================================================================
# EasyTicket
#
# @description: Program to enable a passenger to use the EasyTicket system
# @author: Elisha Lai
# @version: 1.8 30/04/2015
#==============================================================================

# Main Program (main.py)

import Tkinter
from ticket_machine import TicketMachine

# Constants for printing to standard output
origin_station_prompt = 'Enter an origin station: '
destination_station_prompt = 'Enter a destination station: '
invalid_station_msg = 'An invalid station has been entered.'
journey_fare_msg = 'Please pay: '
payment_prompt = 'Enter payment amount: '
ticket_collection_msg = 'Please collect your ticket.'
change_notification_msg = 'Your change is: '
change_collection_msg = 'Please collect your change.'
thank_you_msg = 'Thank you for using the London Underground!'

def main():
    # Creates a ticket machine object.
    ticket_machine = TicketMachine()

    while True:
        ticket_machine.start_session()
	
        # Reads in origin station from standard input until it's a
        # valid station.
        while True:
            origin_station = raw_input(origin_station_prompt)
            if ticket_machine.is_in_network(origin_station):
                break
            print invalid_station_msg
        ticket_machine.set_origin_station(origin_station)
	
        # Reads in destination station from standard input until it's
        # a valid station.
        while True:
	    destination_station = raw_input(destination_station_prompt)
	    if ticket_machine.is_in_network(destination_station):
	        break
	    print invalid_station_msg
        ticket_machine.set_destination_station(destination_station)
    
        ticket_machine.calculate_journey_fare()

        # Reads in payment amount from standard input until the
        # journey fare has been paid in full.
        while True:
    	    owing_amount = ticket_machine.get_remaining_fare_to_be_paid()
    	    print journey_fare_msg + u'\xA3' +'%.2f' % (owing_amount)
    	    payment_amount = raw_input(payment_prompt)
    	    ticket_machine.pay_journey_fare(payment_amount)
    	    if ticket_machine.is_journey_fare_paid():
    	        break
    
        print ticket_collection_msg
        ticket_machine.print_ticket()

        amount_of_change = ticket_machine.return_change()
        if amount_of_change > 0.005: # No change?
    	    print change_notification_msg + u'\xA3' +'%.2f' % (amount_of_change)
    	    print change_collection_msg
    
        print thank_you_msg
        ticket_machine.end_session()


if __name__ == '__main__':
	main()
