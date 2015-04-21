#==============================================================================
# EasyTicket
#
# @description: Module for providing methods to work with Station objects
# @author: Elisha Lai
# @version: 1.3 20/04/2015
#==============================================================================

# Station module (station.py)

# Object definition
class Station:

    'Fields: name, is_open, zones, lines'
    # A Station is an object in which
    # - name is a Str (name of a station)
    # - is_open is a Bool (status indicating whether this station is open/close)
    # - zones is a (listof Int) (zones that this station is located in)
    # - lines is a (listof Str) (lines that this station is part of)

    # Initializes the object.
    def __init__(self, name):
    	self.name = name
	self.is_open = True
	self.zones = set()
	self.lines = set()

    # Concatenates all items in a set s into one string
    def set_to_string(self, s):
    	# Stores the index counter
    	i = 0
    	# Stores the concatenated string to be returned
    	ret_str = ''
    	# Concatenates all items in the set s into one string
        for item in s:
            ret_str += str(item)
            if (i < (len(s) - 1)):
        	ret_str += ', '
            i += 1
        return ret_str

    # Returns a string representation of the object.
    def __repr__(self):
    	zones_str = self.set_to_string(self.zones)
    	lines_str = self.set_to_string(self.lines)
    	return 'Station Name:%s  Is Open?:%r  Zones:%s  Lines:%s' \
               % (self.name, self.is_open, zones_str, lines_str)

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

    # Sets is_open field to True.
    def open(self):
    	isinstance(self, Station)
    	self.is_open = True

    # Sets is_open field to False.
    def close(self):
        isinstance(self, Station)
        self.is_open = False

    # Adds a zone to the zones field.
    def add_zone(self, zone):
    	isinstance(self, Station)
    	self.zones.add(zone)

    # Adds a line to the lines field.
    def add_line(self, line):
    	isinstance(self, Station)
    	self.lines.add(line)
