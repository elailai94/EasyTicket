# =============================================================================
# EasyTicket
#
# @description: Module for providing methods to work with Model objects
# @author: Elisha Lai
# @version: 1.0 16/04/2015
# =============================================================================

from tkinter import Tk
from model import Model


def main():
    # Creates the window
    window = Tk()
    print(window)
    # Creates a model and initializes it
    model = Model()

    # Sets up the menubar in the window

    # Creates all the views and tells them about model and controller

    # Tells model about all the views
    model.add_observer()

if __name__ == '__main__':
    main()
