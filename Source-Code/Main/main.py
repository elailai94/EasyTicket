#==============================================================================
# EasyTicket
#
# @description: Program to enable a passenger to use the EasyTicket system
# @author: Elisha Lai
# @version: 1.8 30/04/2015
#==============================================================================

# Main Program (main.py)

import sys
from command_line import command_line_version
from graphical import graphical_version

if __name__ == '__main__':
   # Indicates whether to run graphical version of the system.
   run_graphical_version = True

   # Processes all optional argument specified at the command-line.
   for arg in sys.argv[1:]:
       if arg == '-text':
   	   run_graphical_version = False
   
   if run_graphical_version:
       graphical_version()
   else:
       command_line_version()
