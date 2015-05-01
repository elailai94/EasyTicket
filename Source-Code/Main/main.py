#==============================================================================
# EasyTicket
#
# @description: Program to enable a passenger to use the EasyTicket system
# @author: Elisha Lai
# @version: 1.8 30/04/2015
#==============================================================================

# Main Program (main.py)

import sys
import Tkinter
from ticket_machine import TicketMachine

# Constants for printing to standard output
origin_station_prompt = 'Enter an origin station: '
destination_station_prompt = 'Enter a destination station: '
invalid_station_msg = 'An invalid station has been entered.'
journey_fare_msg = 'Please pay: '
payment_prompt = 'Enter payment amount: '
refund_notification_msg = 'Your refund is: '
refund_collection_msg = 'Please collect your refund.'
ticket_collection_msg = 'Please collect your ticket.'
change_notification_msg = 'Your change is: '
change_collection_msg = 'Please collect your change.'
thank_you_msg = 'Thank you for using the London Underground!'


# Runs the command-line version of the system.
def command_line_version():
    # Creates a ticket machine object.
    ticket_machine = TicketMachine()

    while True:
    	try:
            ticket_machine.start_session()
            cancel_session = False
	
            # Reads in origin station from standard input until it's a
            # valid station.
            while True:
                origin_station = raw_input(origin_station_prompt)
                if origin_station == 'x': # Cancel session?
            	    cancel_session = True
            	    break
                elif ticket_machine.is_in_network(origin_station):
            	    ticket_machine.set_origin_station(origin_station)
                    break
                else:
            	    print invalid_station_msg
        
	    if not cancel_session:
	        # Reads in destination station from standard input until it's
                # a valid station.
                while True:
	            destination_station = raw_input(destination_station_prompt)
	            if destination_station == 'x': # Cancel session?
	    	        cancel_session = True
	    	        break
	            elif ticket_machine.is_in_network(destination_station):
	                ticket_machine.set_destination_station(destination_station)
	                break
	            else:
	    	        print invalid_station_msg
        
            ticket_machine.calculate_journey_fare()

            if not cancel_session:
                # Reads in payment amount from standard input until the
                # journey fare has been paid in full.
                while True:
    	            owing_amount = ticket_machine.get_remaining_fare_to_be_paid()
    	            print journey_fare_msg + u'\xA3' +'%.2f' % (owing_amount)
    	            payment_amount = raw_input(payment_prompt)
    	            if payment_amount == 'x': # Cancel session?
    	                refund_amount = ticket_machine.refund_amount_of_fare_paid()
    	                if refund_amount > 0.005: # Refund available?
    	        	    print refund_notification_msg + u'\xA3' + '%.2f' % (refund_amount)
    	        	    print refund_collection_msg
    	                cancel_session = True
    	                break
    	            else:
    	            	ticket_machine.pay_journey_fare(payment_amount)
    	            if ticket_machine.is_journey_fare_paid():
    	                break
    
            if not cancel_session:
                print ticket_collection_msg
                ticket_machine.print_ticket()

            if not cancel_session:
                amount_of_change = ticket_machine.return_change()
                if amount_of_change > 0.005: # Change available?
    	            print change_notification_msg + u'\xA3' +'%.2f' % (amount_of_change)
    	            print change_collection_msg
    
            print thank_you_msg

            if cancel_session:
                ticket_machine.end_session('c')
            else:
                ticket_machine.end_session()

        except (EOFError):
        	print '\n'
        	break


# Runs the graphical version of the system.
def graphical_version():
	pass


if __name__ == '__main__':
    # Indicates whether graphical version of the system is run.
    run_graphical_version = True

    # Processes all optional argument specified at the command-line.
    for arg in sys.argv[1:]:
   	if arg == '-text':
   	    run_graphical_version = False
   
    if run_graphical_version:
   	graphical_version()
    else:
        command_line_version()
