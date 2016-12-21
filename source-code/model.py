# =============================================================================
# EasyTicket
#
# @description: Module for providing methods to work with Model objects
# @author: Elisha Lai
# @version: 1.0 16/04/2015
# =============================================================================

from network import Network


class Model:
    # Initializes the object
    def __init__(self):
        self.network = Network("easy_ticket.db")
        self.journey_type = ""
        self.passenger_type = ""
        self.origin_station = ""
        self.destination_station = ""
        self.journey_fare = 0
        self.views = []

    # Returns the journey type
    def get_journey_type(self):
        return self.journey_type

    # Returns the passenger type
    def get_passenger_type(self):
        return self.passenger_type

    # Returns the origin station
    def get_origin_station(self):
        return self.origin_station

    # Returns the destination station
    def get_destination_station(self):
        return self.destination_station

    # Returns the journey fare
    def get_journey_fare(self):
        return self.journey_fare

    # Sets the journey type to a new journey type
    def set_journey_type(self, journey_type):
        self.journey_type = journey_type

    # Sets the passenger type to a new passenger type
    def set_passenger_type(self, passenger_type):
        self.passenger_type = passenger_type

    # Sets the origin station to a new origin station
    def set_origin_station(self, origin_station):
        self.origin_station = origin_station

    # Sets the destination station to a new destination station
    def set_destination_station(self, destination_station):
        self.destination_station = destination_station

    # Resets the model
    def reset(self):
        self.journey_type = ""
        self.passenger_type = ""
        self.origin_station = ""
        self.destination_station = ""
        self.journey_fare = 0

    # Adds a view observer to the model.
    def add_observer(self, a_view):
        self.views.append(a_view)
        a_view.update()

    # Updates all the views observing the model.
    def notify_observers(self):
        for view in self.views:
            view.update()
