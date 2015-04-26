#==============================================================================
# EasyTicket
#
# @description: Module for providing methods to work with Network objects
# @author: Elisha Lai
# @version: 1.2 16/04/2015
#==============================================================================

# Network module (network.py)

from sys import maxint
from station import Station

#{ 'Waterloo': ( StationObj, {'Southwark': 500, 'Westminster': 300} ) }

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
	self.__num_of_stations = 0
	self.__num_of_links = 0
        self.network = {}

    # Builds network field from data files.
    def build_network(self):
    	self.__import_lines()
    	self.__import_links()

    # Reads 
    def __import_lines(self, file_name = 'lines.txt'):
        input_file = file(file_name, 'r')
        # Stores the number of lines
        num_of_lines = int(input_file.readline().strip())
        
        # Reads
        i = 0
        while i < num_of_lines:
            line_file_name = input_file.readline().strip() + '.txt'
            self.__import_stations(line_file_name)
            i += 1

        input_file.close()

    # Reads
    def __import_stations(self, file_name):
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
                self.network[station_name] = (new_station, {})
                self.__num_of_stations += 1
            else:
            	self.network[station_name][0].add_line(line_name)
    	    i += 1

    	input_file.close()

    # Reads
    def __import_links(self, file_name = 'links.txt'):
    	input_file = file(file_name, 'r')
    	# Stores the number of links
    	num_of_links = int(input_file.readline().strip())

    	# Reads
    	i = 0
    	while i < num_of_links:
    		link_info = input_file.readline().strip().split(';')
    		station_a = link_info[0].strip()
    		station_b = link_info[1].strip()
    		link_distance = float(link_info[2].strip())
    		self.__add_link(station_a, station_b, link_distance)
    		i += 1

    	input_file.close()

    # Adds a link between station_a and station_b in the network field
    # and labels the link with distance between the two stations.
    def __add_link(self, station_a, station_b, distance):
    	isinstance(self, Network)
    	if station_a in self.network and\
    	   station_b in self.network and\
    	   (station_a != station_b):
    	    self.network[station_a][1][station_b] = distance
    	    self.network[station_b][1][station_a] = distance
    	    self.__num_of_links += 1

    # Finds the shortest path between station_a and station_b in the
    # network field.
    def shortestpath(self, station_a, station_b, visited = [], distances = {}, predecessors = {}):
    	if station_a in self.network and\
    	   station_b in self.network:
            # we've found our end node, now find the path to it, and return
            if station_a == station_b:
                path = []
                while station_b != None:
                    path.append(station_b)
                    station_b = predecessors.get(station_b, None)
                return distances[station_a], path[::-1]
            # detect if it's the first time through, set current distance to zero
            if not visited:
        	    distances[station_a] = 0
            # process neighbors as per algorithm, keep track of predecessors
            for neighbour in self.network[station_a][1]:
                if neighbour not in visited:
                    neighbor_dist = distances.get(neighbour, maxint)
                    tentative_dist = distances[station_a] + self.network[station_a][1][neighbour]
                    if tentative_dist < neighbor_dist:
                        distances[neighbour] = tentative_dist
                        predecessors[neighbour] = station_a
            # neighbors processed, now mark the current node as visited
            visited.append(station_a)
            # finds the closest unvisited node to the start
            unvisiteds = dict((k, distances.get(k, maxint)) for k in self.network if k not in visited)
            closestnode = min(unvisiteds, key = unvisiteds.get)
            # now we can take the closest node and recurse, making it current
            return self.shortestpath(closestnode, station_b, visited, distances, predecessors)
