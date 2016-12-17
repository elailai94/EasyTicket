# =============================================================================
# EasyTicket
#
# @description: Module for providing methods to work with Model objects
# @author: Elisha Lai
# @version: 1.0 16/04/2015
# =============================================================================

from network import Network


class Model:
    # Initializes the object.
    def __init__(self):
        self.network = Network("easy_ticket.db")
        self.journey_type = ""
        self.origin_station = ""
        self.destination_station = ""
        self.journey_fare = 0
        self.views = []

    # Adds a view observer to the model.
    def add_observer(self, a_view):
        self.views.append(a_view)
        a_view.update()

    # Updates all the views observing the model.
    def notify_observers(self):
        for view in self.views:
            view.update()
