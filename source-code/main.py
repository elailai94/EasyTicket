# =============================================================================
# EasyTicket
#
# @description: Module for providing methods to work with Model objects
# @author: Elisha Lai
# @version: 1.0 16/04/2015
# =============================================================================

from tkinter import Tk
from tkinter import Menu
from model import Model


def main():
    # Creates the window
    window = Tk()
    window.title("Easy Ticket")

    # Creates a model and initializes it
    model = Model()

    # Sets up the menubar in the window

    # Creates all the views and tells them about model and controller

    # Tells model about all the views
    #model.add_observer()
    
    # Loop
    window.mainloop()

def make_menu_bar(window):
    menu_bar = Menu(window)
    
    file_menu = Menu(menu_bar)
    file_menu.add_cascade(label="File", menu=file_menu)

if __name__ == '__main__':
    main()
