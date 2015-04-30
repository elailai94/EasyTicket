#==============================================================================
# EasyTicket
#
# @description: Program
# @author: Elisha Lai
# @version: 1.2 26/04/2015
#==============================================================================

# Main Program (main.py)

import Tkinter
from ticket_machine import TicketMachine

origin_station_prompt = 'Enter an origin station: '
destination_station_prompt = 'Enter a destination station: '
invalid_station_msg = 'An invalid station has been entered.'
payment_msg = 'Enter payment amount: '

def main():
	ticket_machine = TicketMachine()
	ticket_machine.start_session()
	station_a = raw_input(origin_station_prompt)
	while not ticket_machine.is_in_network(station_a):
		print invalid_station_msg
		station_a = raw_input(origin_station_prompt)
	ticket_machine.set_origin_station(station_a)
	station_b = raw_input(destination_station_prompt)
	while not ticket_machine.is_in_network(station_b):
		print invalid_station_msg
		station_b = raw_input(destination_station_prompt)
	ticket_machine.set_destination_station(station_b)
	ticket_machine.calculate_journey_fare()
	amt_of_money_inserted = raw_input(payment_msg)
	ticket_machine.pay_journey_fare(amt_of_money_inserted)
	print ticket_machine.refund_amount_of_fare_paid()
	#ticket_machine.print_ticket()
	#print 'Your change is: %.2f' % (ticket_machine.return_change())
	print ticket_machine
	ticket_machine.end_session()
	print ticket_machine

if __name__ == '__main__':
	main()
