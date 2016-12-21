# =============================================================================
# EasyTicket
#
# @description: Module for providing methods to work with Model objects
# @author: Elisha Lai
# @version: 1.0 16/04/2015
# =============================================================================


class View:
    # Initializes the object
    def __init__(self, window, model):
        self.window = window
        self.model = model
        self.layout_view()
        self.register_controllers()

    def layout_view(self):
        pass

    def register_controller(self):
        pass
