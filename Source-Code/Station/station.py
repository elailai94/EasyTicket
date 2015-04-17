#==============================================================================
# EasyTicket
#
# @description: Module for providing methods to work with Station objects
# @author: Elisha Lai
# @version: 1.2 16/04/2015
#==============================================================================

# Station module (station.py)

# Object definition
class Station:

    'Fields: name, zone, lines'
    # A Station is an object in which
    # - name is a Str (name of a station)
    # - zone is an Int (zone that this station is located in)
    # - lines is a (listof Str) (lines that this station is part of)

    # Initializes the object.
    def __init__(self, name, zone):
	self.name = name
	self.zone = zone
        self.lines = []

    # Returns a string representation of the object.
    def __repr__(self):
    	i = 0
    	lines_str = ''
    	for line in self.lines:
            lines_str += line
    	    if (i < (len(self.lines) - 1)):
    	        lines_str += ', '
            i += 1
    	return 'Station Name:%s  Zone:%d  Lines:%s' \
               % (self.name, self.zone, lines_str)

    # Returns True if self and other represent stations with the same name
    # and False otherwise.
    def __eq__(self, other):
    	return isinstance(self, Station) and \
    	       isinstance(other, Station) and \
    	       self.name == other.name

    # Returns True if self and other represent stations with different names
    # and False otherwise.
    def __ne__(self, other):
    	return self != other

    # Adds a line to the lines field.
    def add_line(self, line):
    	isinstance(self, Station)
    	self.lines.append(line)
