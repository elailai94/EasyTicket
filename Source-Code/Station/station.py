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

    'Fields: name, is_open, zones, lines'
    # A Station is an object in which:
    # - name is a Str (name of this station)
    # - is_open is a Bool (status indicating whether this station is
    #	open/close)
    # - zones is a (listof Int) (fare zones that this station is part of)
    # - lines is a (listof Str) (lines that this station is part of)


    # Initializes the object.
    def __init__(self, name):
	self.__name = name
	self.__is_open = True
	self.__zones = set()
	self.__lines = set()


    # Returns a string representation of the object.
    def __repr__(self):
    	zones_str = self.__set_to_string(self.__zones)
    	lines_str = self.__set_to_string(self.__lines)
    	return 'Station Name:%s  Is Open?:%r  Zones:%s  Lines:%s' \
               % (self.__name, self.__is_open, zones_str, lines_str)


    # Concatenates all items in a set s into one string
    def __set_to_string(self, s):
    	# Stores the concatenated string to be returned
    	ret_str = ''
    	
    	# Concatenates all items in the set s into one string
    	i = 0
        for item in s:
            ret_str += str(item)
            if (i < (len(s) - 1)):
                ret_str += ', '
            i += 1
        return ret_str


    # Returns True if self and other represent stations with the same name
    # and False otherwise.
    def __eq__(self, other):
    	return isinstance(self, Station) and \
    	       isinstance(other, Station) and \
    	       self.__name == other.__name


    # Returns True if self and other represent stations with different names
    # and False otherwise.
    def __ne__(self, other):
    	return self != other

    
    # Sets is_open field to True.
    def open(self):
    	isinstance(self, Station)
    	self.__is_open = True


    # Sets is_open field to False.
    def close(self):
        isinstance(self, Station)
        self.__is_open = False


    # Adds a zone to the zones field.
    def add_zone(self, zone):
    	isinstance(self, Station)
    	self.__zones.add(zone)


    # Adds a line to the lines field.
    def add_line(self, line):
    	isinstance(self, Station)
    	self.__lines.add(line)
