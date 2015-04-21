#==============================================================================
# EasyTicket
#
# @description: Module for providing methods to work with Network objects
# @author: Elisha Lai
# @version: 1.2 16/04/2015
#==============================================================================

# Network module (network.py)

from station import Station

#{ 'Waterloo': ( StationObj, [['Southwark', 500],['Westminster', 300]] ) }

# Object definition
class Network:

    'Fields: num_of_stations, num_of_links, network'
    # A Network is an object in which:
    # - num_of_stations is an Int (number of stations in this network)
    # - num_of_links is an Int (number of links between stations
    #	in this network)
    # - network is a Stationdict (network)

    # A stationdict is a dictionary where:
    # - the keys are Str values 
    # - the values themselves are 2-tuple

    # Initializes the object.
    def __init__(self):
	      self.num_of_stations = 0
	      self.num_of_links = 0
        self.network = {}

    # Adds a station to the network field.
    def add_station(self, station):
	      isinstance(self, Network) and \
        isinstance(station, Station)
        self.network[station.name] = (station, [])
        self.num_of_stations += 1

    # Adds a link between station_a and station_b in the network field
    # and labels the link with distance between the two stations.
    def add_link(self, station_a, station_b, distance):
    	  isinstance(self, Network)
    	  if (station_a != station_b):
    	      self.network[station_a][1].append([station_b, distance])
    	      self.network[station_b][1].append([station_a, distance])
    	      self.num_of_links += 1

    # Reads 
    def import_lines(self, file_name = 'lines.txt'):
        input_file = file(file_name, 'r')
        # Stores the number of lines
        num_of_lines = int(input_file.readline().strip())
        
        # Reads
        i = 0
        while i < num_of_lines:
            line_file_name = input_file.readline().strip() + '.txt'
            self.import_stations(line_file_name)
            i += 1

        input_file.close()

    # Reads
    def import_stations(self, file_name):
    	input_file = file(file_name, 'r')
    	# Stores the name of the line
    	line_name = input_file.readline().strip()
    	# Stores the number of stations in the line
    	num_of_stations = int(input_file.readline().strip())
    	
    	# Reads 
    	i = 0
    	while i < num_of_stations:
    	    station_info = input_file.readline().strip().split(';')
          station_name = station_info[0]

          if station_name not in self.network:
            	new_station = Station(station_name)
            	new_station.add_line(line_name)
            	station_zones = station_info[1].split('+')
              for zone in station_zones:
                	new_station.add_zone(int(zone))
              self.add_station(new_station)
          else:
            	self.network[station_name][0].add_line(line_name)
    	    i += 1

    	input_file.close()
